#!/usr/bin/env python3
"""
Simple documentation search API for MCP chatbot integration
Provides search functionality over Appcircle documentation
Now uses structured JSON files from the existing workflow
"""

import json
import re
import os
from typing import List, Dict, Any
from pathlib import Path


class QueryProcessor:
    """
    Handles query preprocessing, abbreviation expansion, and synonym mapping.
    
    This class provides a rule-based approach to enhance search queries by:
    1. Expanding common abbreviations (e.g., PAT → Personal Access Token)
    2. Converting question patterns to searchable terms
    3. Adding relevant synonyms to improve matching
    4. Cleaning and optimizing the final query
    
    🤖 **LLM Enhancement Opportunity:**
    This manual rule-based system can be replaced with LLM-powered query processing:
    - Use embedding models for semantic similarity
    - Implement contextual understanding of user intent  
    - Dynamic synonym generation based on documentation content
    - Natural language query reformulation
    
    Example LLM integration:
    ```python
    def llm_process_query(self, query: str) -> str:
        prompt = f'''
        Convert this user query into optimal search terms for documentation:
        Query: "{query}"
        
        Consider:
        - Expand abbreviations (PAT=Personal Access Token)
        - Add synonyms and related terms
        - Focus on actionable keywords
        
        Return only the enhanced search terms:
        '''
        return llm_client.complete(prompt)
    ```
    
    Migration Path:
    1. Keep this class as fallback for simple queries
    2. Add LLM processing for complex/ambiguous queries  
    3. A/B test performance improvements
    4. Gradually transition to full LLM processing
    """
    
    def __init__(self):
        # Abbreviation mappings
        self.abbreviations = {
            'pat': 'personal access token',
            'api': 'application programming interface',
            'cli': 'command line interface',
            'ci': 'continuous integration',
            'cd': 'continuous deployment',
            'sdk': 'software development kit',
            'ide': 'integrated development environment',
            'ui': 'user interface',
            'ux': 'user experience',
            'ssl': 'secure socket layer',
            'tls': 'transport layer security',
            'ssh': 'secure shell',
            'jwt': 'json web token',
            'oauth': 'open authorization',
            'saml': 'security assertion markup language',
            'sso': 'single sign on',
            'mfa': '2fa two factor authentication multi factor authentication',
            'ios': 'ios apple',
            'apk': 'android package',
            'ipa': 'ios package archive',
            'aab': 'android app bundle',
            'xcode': 'xcode ios development',
            'gradle': 'android gradle build',
            'cocoapods': 'ios cocoapods dependency',
            'carthage': 'ios carthage dependency',
            'spm': 'swift package manager',
            'git': 'version control repository',
            'github': 'git repository hosting',
            'gitlab': 'git repository hosting',
            'bitbucket': 'git repository hosting',
            'azure': 'microsoft azure devops',
            'aws': 'amazon web services cloud',
            'gcp': 'google cloud platform',
        }
        
        # Synonym and context mappings
        self.synonyms = {
            'create': ['make', 'generate', 'add', 'setup', 'configure', 'build', 'new'],
            'setup': ['configure', 'install', 'initialize', 'create'],
            'connect': ['link', 'integrate', 'attach', 'bind'],
            'deploy': ['publish', 'release', 'distribute', 'upload'],
            'build': ['compile', 'package', 'assemble'],
            'test': ['testing', 'validation', 'verification'],
            'profile': ['configuration', 'settings', 'config'],
            'workflow': ['pipeline', 'process', 'flow'],
            'repository': ['repo', 'source', 'code'],
            'branch': ['version', 'variant'],
            'certificate': ['cert', 'signing', 'provisioning'],
            'key': ['token', 'credential', 'authentication'],
        }
        
        # Common question patterns
        self.question_patterns = {
            'how to create': 'create setup configure',
            'how to setup': 'setup configure install',
            'how to connect': 'connect integrate configure',
            'how to deploy': 'deploy publish release',
            'how to build': 'build compile configuration',
            'what is': 'overview introduction about',
            'where is': 'location find access',
        }
    
    def process_query(self, query: str) -> str:
        """
        Process and enhance the query using rule-based transformations.
        
        Args:
            query (str): Original user query (e.g., "create the PAT")
            
        Returns:
            str: Enhanced query (e.g., "create setup configure personal access token make generate add")
            
        Processing Steps:
        1. Handle question patterns ("how to create" → "create setup configure")
        2. Expand abbreviations ("PAT" → "personal access token")  
        3. Add relevant synonyms ("create" → "make generate add")
        4. Clean and optimize final query
        
        🤖 **LLM Replacement:**
        This entire method can be replaced with a single LLM call:
        
        ```python
        def llm_process_query(self, query: str) -> str:
            # Single LLM call handles all processing steps intelligently
            return openai_client.chat.completions.create(
                model="gpt-4",
                messages=[{
                    "role": "system", 
                    "content": "Convert user queries to optimal documentation search terms. Expand abbreviations, add synonyms, focus on actionable keywords."
                }, {
                    "role": "user",
                    "content": query
                }]
            ).choices[0].message.content
        ```
        """
        if not query.strip():
            return query
            
        original_query = query.lower().strip()
        processed_query = original_query
        
        # Step 1: Handle question patterns
        processed_query = self._handle_question_patterns(processed_query)
        
        # Step 2: Expand abbreviations
        processed_query = self._expand_abbreviations(processed_query)
        
        # Step 3: Add synonyms for better matching
        processed_query = self._add_synonyms(processed_query)
        
        # Step 4: Clean and optimize
        processed_query = self._clean_query(processed_query)
        
        return processed_query
    
    def _handle_question_patterns(self, query: str) -> str:
        """Convert common question patterns to searchable terms"""
        for pattern, replacement in self.question_patterns.items():
            if pattern in query:
                query = query.replace(pattern, replacement)
        return query
    
    def _expand_abbreviations(self, query: str) -> str:
        """
        Expand known abbreviations using predefined mapping.
        
        🤖 **LLM Enhancement:**
        Replace with context-aware abbreviation expansion:
        - Understand domain-specific abbreviations dynamically
        - Handle context-dependent expansions (CI could mean Continuous Integration or Configuration Item)
        - Learn new abbreviations from documentation content automatically
        """
        words = query.split()
        expanded_words = []
        
        for word in words:
            # Remove punctuation for matching
            clean_word = re.sub(r'[^\w]', '', word.lower())
            if clean_word in self.abbreviations:
                expanded_words.append(self.abbreviations[clean_word])
            else:
                expanded_words.append(word)
        
        return ' '.join(expanded_words)
    
    def _add_synonyms(self, query: str) -> str:
        """
        Add relevant synonyms to improve matching using predefined mappings.
        
        🤖 **LLM Enhancement:**
        Replace with semantic similarity matching:
        - Use embedding models to find contextually relevant terms
        - Generate synonyms based on actual documentation content
        - Understand semantic relationships beyond simple word mappings
        - Adapt to domain-specific language usage
        """
        words = query.split()
        enhanced_words = list(words)  # Start with original words
        
        for word in words:
            clean_word = word.lower()
            if clean_word in self.synonyms:
                # Add up to 2 most relevant synonyms
                enhanced_words.extend(self.synonyms[clean_word][:2])
        
        return ' '.join(enhanced_words)
    
    def _clean_query(self, query: str) -> str:
        """Clean and optimize the final query"""
        # Remove extra whitespace
        query = re.sub(r'\s+', ' ', query).strip()
        
        # Remove common stop words that don't help with search
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with'}
        words = [word for word in query.split() if word.lower() not in stop_words]
        
        return ' '.join(words)


class DocsSearchAPI:
    def __init__(self, structured_docs_dir: str = "structured_docs"):
        """Initialize with structured documentation files"""
        self.structured_docs_dir = structured_docs_dir
        self.index = self._load_structured_docs()
        self.query_processor = QueryProcessor()
        
    def _load_structured_docs(self) -> Dict[str, Any]:
        """Load all structured JSON files and combine them"""
        combined_docs = []
        sections_info = {}
        
        if not os.path.exists(self.structured_docs_dir):
            print(f"❌ Structured docs directory '{self.structured_docs_dir}' not found")
            return {"documents": [], "sections": {}}
        
        try:
            for filename in os.listdir(self.structured_docs_dir):
                if not filename.endswith('.json'):
                    continue
                    
                filepath = os.path.join(self.structured_docs_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    section_data = json.load(f)
                
                section_name = section_data.get('section', filename.replace('.json', ''))
                sections_info[section_name] = {
                    'title': section_data.get('section_title', section_name.title()),
                    'total_documents': section_data.get('total_documents', 0),
                    'filename': filename
                }
                
                # Add section info to each document
                for doc in section_data.get('documents', []):
                    doc['section'] = section_name
                    doc['section_title'] = section_data.get('section_title', section_name.title())
                    combined_docs.append(doc)
            
            print(f"✅ Loaded {len(combined_docs)} documents from {len(sections_info)} sections")
            return {
                "documents": combined_docs,
                "sections": sections_info,
                "total_documents": len(combined_docs)
            }
            
        except Exception as e:
            print(f"❌ Error loading structured docs: {e}")
            return {"documents": [], "sections": {}}
    
    def search(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Search documentation with enhanced query processing and relevance scoring"""
        if not query.strip():
            return []
        
        # Process the query to expand abbreviations and add synonyms
        original_query = query.strip()
        processed_query = self.query_processor.process_query(original_query)
        
        # Use both original and processed query for comprehensive search
        combined_query = f"{original_query} {processed_query}".lower().strip()
        
        results = []
        
        for doc in self.index.get("documents", []):
            score = self._calculate_relevance(doc, combined_query)
            if score > 0:
                result = {
                    "id": doc["id"],
                    "title": doc["title"],
                    "description": doc.get("description", ""),
                    "url": doc["url"],
                    "section": doc["section"],
                    "relevance_score": score
                }
                results.append(result)
        
        # Sort by relevance score (higher is better)
        results.sort(key=lambda x: x["relevance_score"], reverse=True)
        
        # Add debug info for the first few results
        if results:
            print(f"🔍 Query: '{original_query}' → Enhanced: '{processed_query}'")
            print(f"📊 Top result: {results[0]['title']} (score: {results[0]['relevance_score']:.1f})")
        
        return results[:max_results]
    
    def _calculate_relevance(self, doc: Dict[str, Any], query: str) -> float:
        """Calculate relevance score for a document"""
        score = 0.0
        query_words = set(query.lower().split())
        
        # Title match (highest weight)
        title = doc.get("title", "").lower()
        title_words = set(re.findall(r'\w+', title))
        title_matches = len(query_words.intersection(title_words))
        score += title_matches * 10
        
        # Exact title phrase match
        if query in title:
            score += 20
        
        # Description match (medium weight) - structured docs use 'description' instead of 'summary'
        description = doc.get("description", "").lower()
        desc_words = set(re.findall(r'\w+', description))
        desc_matches = len(query_words.intersection(desc_words))
        score += desc_matches * 5
        
        # Content match (lower weight)
        content = doc.get("content", "").lower()
        content_words = set(re.findall(r'\w+', content))
        content_matches = len(query_words.intersection(content_words))
        score += content_matches * 1
        
        # Exact phrase in content
        if query in content:
            score += 5
        
        # Tags match (medium weight)
        tags = doc.get("tags", [])
        if isinstance(tags, list):
            tag_text = " ".join(str(tag).lower() for tag in tags)
            tag_words = set(re.findall(r'\w+', tag_text))
            tag_matches = len(query_words.intersection(tag_words))
            score += tag_matches * 7
        
        return score
    
    def get_document_by_id(self, doc_id: str) -> Dict[str, Any]:
        """Get full document content by ID"""
        for doc in self.index.get("documents", []):
            if doc["id"] == doc_id:
                return doc
        return {}
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """Get all available sections with metadata"""
        sections_info = self.index.get("sections", {})
        return [{
            "name": section_name,
            "title": info["title"],
            "total_documents": info["total_documents"]
        } for section_name, info in sections_info.items()]
    
    def search_by_section(self, section: str, max_results: int = 20) -> List[Dict[str, Any]]:
        """Get all documents from a specific section"""
        results = []
        for doc in self.index.get("documents", []):
            if doc.get("section", "general") == section:
                result = {
                    "id": doc["id"],
                    "title": doc["title"],
                    "description": doc.get("description", ""),
                    "url": doc["url"],
                    "section": doc["section"]
                }
                results.append(result)
        
        # Sort by title
        results.sort(key=lambda x: x["title"])
        return results[:max_results]


def main():
    """Command line interface for testing"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python docs_search_api.py '<search_query>'")
        print("Example: python docs_search_api.py 'build profile'")
        return
    
    query = sys.argv[1]
    api = DocsSearchAPI()
    results = api.search(query)
    
    print(f"🔍 Search results for: '{query}'")
    print(f"📊 Found {len(results)} results")
    print("-" * 80)
    
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['title']}")
        print(f"   📑 {result['description']}")
        print(f"   🔗 {result['url']}")
        print(f"   📂 Section: {result['section']} | Score: {result['relevance_score']:.1f}")
        print()


if __name__ == "__main__":
    main()