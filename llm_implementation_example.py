#!/usr/bin/env python3
"""
Practical LLM Implementation Example - Migration from Current System

This script demonstrates how to implement Claude Chat-style documentation search
by migrating from the current rule-based QueryProcessor to full LLM integration.

Usage:
    pip install openai pinecone-client chromadb fastapi uvicorn
    python3 llm_implementation_example.py
"""

import asyncio
import json
import os
import time
import uuid
from typing import List, Dict, Any, Optional
from datetime import datetime
import hashlib

# Core dependencies for LLM integration
try:
    import openai
    import chromadb
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    import uvicorn
except ImportError as e:
    print(f"❌ Missing dependencies: {e}")
    print("💡 Install with: pip install openai chromadb fastapi uvicorn")
    exit(1)

# Import current system for migration
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from docs_search_api import DocsSearchAPI, QueryProcessor


class LLMDocumentationChat:
    """
    Complete LLM implementation for Claude Chat-style documentation search.
    Demonstrates migration path from current rule-based system.
    """
    
    def __init__(self, openai_api_key: str = None):
        """Initialize LLM chat system"""
        
        # Initialize OpenAI client
        self.openai_client = openai.OpenAI(
            api_key=openai_api_key or os.getenv('OPENAI_API_KEY')
        )
        
        # Initialize vector database (using ChromaDB for simplicity)
        self.chroma_client = chromadb.Client()
        self.collection_name = "appcircle_docs"
        
        # Try to get existing collection or create new one
        try:
            self.collection = self.chroma_client.get_collection(self.collection_name)
            print(f"✅ Using existing collection: {self.collection_name}")
        except:
            self.collection = self.chroma_client.create_collection(self.collection_name)
            print(f"✅ Created new collection: {self.collection_name}")
        
        # Keep current system for comparison
        self.current_search = DocsSearchAPI()
        self.rule_processor = QueryProcessor()
        
        # Conversation management
        self.conversations = {}
        
        # Configuration
        self.embedding_model = "text-embedding-3-small"  # Cost-effective option
        self.chat_model = "gpt-4o-mini"  # Good balance of quality and cost
        
    async def initialize_embeddings(self):
        """
        Initialize vector embeddings from current documentation.
        Migrates from keyword search to semantic search.
        """
        print("🔄 Initializing vector embeddings...")
        
        documents = self.current_search.index.get('documents', [])
        print(f"📄 Processing {len(documents)} documents...")
        
        # Process documents in batches to avoid rate limits
        batch_size = 50
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i+batch_size]
            await self._embed_document_batch(batch)
            print(f"✅ Processed batch {i//batch_size + 1}/{(len(documents) + batch_size - 1)//batch_size}")
        
        print(f"🎉 Embedding initialization complete! {len(documents)} documents embedded.")
    
    async def _embed_document_batch(self, documents: List[Dict]):
        """Embed a batch of documents"""
        
        # Prepare texts for embedding
        texts = []
        metadatas = []
        ids = []
        
        for doc in documents:
            # Create rich text for embedding
            text_for_embedding = f"""
            Title: {doc['title']}
            Description: {doc.get('description', '')}
            Section: {doc.get('section', '')}
            Content: {doc.get('content', '')}
            """.strip()
            
            texts.append(text_for_embedding)
            metadatas.append({
                'title': doc['title'],
                'description': doc.get('description', ''),
                'url': doc['url'],
                'section': doc['section'],
                'content': doc.get('content', '')[:2000]  # Limit content length
            })
            ids.append(doc['id'])
        
        # Add to ChromaDB (automatically handles embedding generation)
        self.collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )
    
    async def semantic_search(self, query: str, top_k: int = 10) -> List[Dict]:
        """
        Perform semantic search using vector embeddings.
        Replaces keyword-based search with understanding of meaning.
        """
        
        # Search using ChromaDB's built-in embedding and similarity
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )
        
        # Convert results to our document format
        documents = []
        for i in range(len(results['ids'][0])):
            doc = {
                'id': results['ids'][0][i],
                'title': results['metadatas'][0][i]['title'],
                'description': results['metadatas'][0][i]['description'],
                'url': results['metadatas'][0][i]['url'], 
                'section': results['metadatas'][0][i]['section'],
                'content': results['metadatas'][0][i]['content'],
                'similarity_score': 1 - results['distances'][0][i]  # Convert distance to similarity
            }
            documents.append(doc)
        
        return documents
    
    async def process_query_with_llm(self, query: str, conversation_history: List[Dict] = None) -> Dict:
        """
        Process user query with LLM to understand intent and enhance search.
        Replaces rule-based QueryProcessor with contextual understanding.
        """
        
        system_prompt = """You are an expert at understanding user queries about mobile CI/CD and Appcircle documentation.

Your job is to analyze user queries and help find the most relevant documentation.

Analyze the query and return JSON with:
{
    "user_intent": "what the user wants to accomplish",
    "enhanced_query": "optimized search terms for finding relevant docs",
    "query_type": "tutorial|reference|troubleshooting|concept|comparison",
    "confidence": 0.95,
    "key_concepts": ["concept1", "concept2"],
    "suggested_sections": ["section1", "section2"]
}

Focus on understanding the user's actual goal, not just the literal query."""

        messages = [{"role": "system", "content": system_prompt}]
        
        # Add conversation history for context
        if conversation_history:
            for msg in conversation_history[-4:]:  # Last 4 messages for context
                messages.append(msg)
        
        messages.append({"role": "user", "content": f"Query: {query}"})
        
        try:
            response = await self.openai_client.chat.completions.create(
                model=self.chat_model,
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.3
            )
            
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"⚠️ LLM query processing failed: {e}")
            # Fallback to rule-based processing
            return {
                "user_intent": "Unknown - using fallback",
                "enhanced_query": self.rule_processor.process_query(query),
                "query_type": "unknown",
                "confidence": 0.5
            }
    
    async def synthesize_answer(self, query: str, documents: List[Dict], conversation_history: List[Dict] = None) -> Dict:
        """
        Generate Claude Chat-style comprehensive answer from multiple documents.
        This is the core feature that transforms search results into conversational responses.
        """
        
        # Prepare context from top documents
        context_sections = []
        for i, doc in enumerate(documents[:5]):  # Top 5 most relevant
            context_sections.append(f"""
Document {i+1}: {doc['title']}
Section: {doc['section']}
URL: {doc['url']}
Similarity: {doc.get('similarity_score', 'N/A'):.3f}
Content: {doc.get('content', doc.get('description', ''))}
""")
        
        context = "\n---\n".join(context_sections)
        
        system_prompt = """You are Claude, an expert assistant helping users with Appcircle mobile CI/CD documentation.

Your job is to provide comprehensive, accurate answers based on the provided documentation context.

Guidelines:
1. Answer directly and thoroughly based on ONLY the provided context
2. Include step-by-step instructions when applicable  
3. Use markdown formatting for clarity
4. Reference specific documentation sections
5. If information is incomplete in the context, clearly state limitations
6. Be conversational but precise
7. Include code examples when available in the context
8. Provide actionable guidance

Format your response as a helpful explanation, not just a summary of documents."""

        messages = [{"role": "system", "content": system_prompt}]
        
        # Add conversation history for context
        if conversation_history:
            for msg in conversation_history[-6:]:
                messages.append(msg)
        
        messages.append({
            "role": "user", 
            "content": f"""
User Query: {query}

Documentation Context:
{context}

Please provide a comprehensive answer based on this documentation context."""
        })
        
        try:
            response = await self.openai_client.chat.completions.create(
                model=self.chat_model,
                messages=messages,
                max_tokens=1500,
                temperature=0.3
            )
            
            return {
                "answer": response.choices[0].message.content,
                "tokens_used": response.usage.total_tokens,
                "model": self.chat_model
            }
        except Exception as e:
            return {
                "answer": f"❌ Error generating answer: {e}",
                "tokens_used": 0,
                "model": "error"
            }
    
    async def chat(self, query: str, conversation_id: str = None) -> Dict:
        """
        Main chat interface - complete Claude Chat-style interaction.
        """
        start_time = time.time()
        
        if not conversation_id:
            conversation_id = str(uuid.uuid4())
        
        # Get conversation history
        history = self.conversations.get(conversation_id, [])
        
        print(f"💬 Processing query: '{query}'")
        
        # Step 1: Process query with LLM
        print("🧠 Processing query with LLM...")
        processed_query = await self.process_query_with_llm(query, history)
        
        # Step 2: Semantic search for relevant documents  
        print("🔍 Performing semantic search...")
        documents = await self.semantic_search(
            processed_query['enhanced_query'], 
            top_k=10
        )
        
        # Step 3: Generate comprehensive answer
        print("✍️ Synthesizing answer...")
        answer_result = await self.synthesize_answer(query, documents, history)
        
        # Step 4: Update conversation history
        self.conversations[conversation_id] = history + [
            {"role": "user", "content": query},
            {"role": "assistant", "content": answer_result['answer']}
        ]
        
        response_time = time.time() - start_time
        
        return {
            "conversation_id": conversation_id,
            "query": query,
            "processed_query": processed_query,
            "answer": answer_result['answer'],
            "sources": [
                {
                    "title": doc['title'],
                    "url": doc['url'],
                    "section": doc['section'], 
                    "similarity": doc.get('similarity_score', 0)
                }
                for doc in documents[:3]
            ],
            "response_time": response_time,
            "tokens_used": answer_result.get('tokens_used', 0)
        }
    
    async def compare_with_current_system(self, query: str):
        """
        Compare LLM system with current rule-based system.
        Demonstrates the improvements achieved.
        """
        print(f"\n🔬 COMPARISON: '{query}'")
        print("=" * 60)
        
        # Current system results
        print("📊 CURRENT SYSTEM (Rule-based):")
        current_results = self.current_search.search(query, max_results=3)
        for i, result in enumerate(current_results, 1):
            print(f"  {i}. {result['title']} (Score: {result['relevance_score']:.1f})")
        
        # LLM system results  
        print("\n🤖 LLM SYSTEM (Semantic + Synthesis):")
        llm_result = await self.chat(query)
        
        print(f"Query Processing:")
        print(f"  Intent: {llm_result['processed_query'].get('user_intent', 'N/A')}")
        print(f"  Enhanced: {llm_result['processed_query'].get('enhanced_query', 'N/A')}")
        
        print(f"\nTop Sources:")
        for i, source in enumerate(llm_result['sources'], 1):
            print(f"  {i}. {source['title']} (Similarity: {source['similarity']:.3f})")
        
        print(f"\nGenerated Answer:")
        print(f"  {llm_result['answer'][:200]}..." if len(llm_result['answer']) > 200 else f"  {llm_result['answer']}")
        
        print(f"\nPerformance:")
        print(f"  Response Time: {llm_result['response_time']:.2f}s")
        print(f"  Tokens Used: {llm_result['tokens_used']}")


# FastAPI Web Interface
app = FastAPI(title="LLM Documentation Chat", description="Claude Chat-style documentation search")

# Global chat system instance
chat_system = None

class ChatRequest(BaseModel):
    query: str
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    conversation_id: str
    query: str
    answer: str
    sources: List[Dict]
    response_time: float
    tokens_used: int

@app.on_event("startup")
async def initialize_system():
    """Initialize the LLM chat system on startup"""
    global chat_system
    
    # Check for OpenAI API key
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ OPENAI_API_KEY environment variable not set")
        print("💡 Set it with: export OPENAI_API_KEY='your-api-key'")
        return
    
    chat_system = LLMDocumentationChat()
    print("🚀 Initializing embeddings...")
    await chat_system.initialize_embeddings()
    print("✅ LLM Chat system ready!")

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Claude Chat-style conversational endpoint"""
    if not chat_system:
        raise HTTPException(status_code=503, detail="System not initialized - missing OpenAI API key")
    
    try:
        result = await chat_system.chat(
            query=request.query,
            conversation_id=request.conversation_id
        )
        
        return ChatResponse(**result)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")

@app.get("/compare")
async def compare_systems(query: str):
    """Compare current system vs LLM system"""
    if not chat_system:
        raise HTTPException(status_code=503, detail="System not initialized")
    
    await chat_system.compare_with_current_system(query)
    return {"status": "comparison printed to console"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy" if chat_system else "initializing",
        "system": "LLM Documentation Chat",
        "openai_configured": bool(os.getenv('OPENAI_API_KEY'))
    }


async def demo_llm_system():
    """
    Demonstrate the LLM system capabilities.
    Run this to see the system in action.
    """
    print("🚀 LLM Documentation Chat Demo")
    print("=" * 50)
    
    # Check API key
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ OpenAI API key not found!")
        print("💡 Set your API key: export OPENAI_API_KEY='your-key'")
        print("🔗 Get key at: https://platform.openai.com/api-keys")
        return
    
    # Initialize system
    chat = LLMDocumentationChat()
    print("🔄 Initializing embeddings (this may take a few minutes)...")
    await chat.initialize_embeddings()
    
    # Test queries
    test_queries = [
        "create the PAT",
        "how to setup CI/CD for iOS",
        "what is the difference between build profile and workflow",
        "troubleshoot Android build failures"
    ]
    
    print("\n🧪 Testing Queries:")
    print("=" * 50)
    
    for query in test_queries:
        print(f"\n💬 Query: '{query}'")
        print("-" * 40)
        
        # Compare with current system
        await chat.compare_with_current_system(query)
        
        print("\n" + "="*60)
    
    print("\n🎉 Demo completed!")
    print("\n🚀 To start the web API:")
    print("   export OPENAI_API_KEY='your-key'")  
    print("   python3 llm_implementation_example.py")
    print("   # Then visit: http://localhost:8001/docs")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        # Run demonstration
        asyncio.run(demo_llm_system())
    else:
        # Start web API
        if not os.getenv('OPENAI_API_KEY'):
            print("❌ OpenAI API key required!")
            print("💡 Set it with: export OPENAI_API_KEY='your-api-key'")
            print("🔗 Get key at: https://platform.openai.com/api-keys")
            print("\n🧪 Or run demo: python3 llm_implementation_example.py demo")
        else:
            print("🚀 Starting LLM Documentation Chat API...")
            print("🔗 API docs: http://localhost:8001/docs")
            print("💬 Chat: POST http://localhost:8001/chat")
            uvicorn.run(app, host="0.0.0.0", port=8001)