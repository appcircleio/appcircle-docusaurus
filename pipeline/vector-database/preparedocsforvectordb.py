import json
import re
from typing import List, Dict, Any, Optional, Union
from pathlib import Path
import logging
from dataclasses import dataclass
import hashlib
import numpy as np
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class ProcessedDocument:
    """Structured representation of a processed document"""
    id: str
    title: str
    content: str
    section: str
    description: Optional[str] = None
    url: Optional[str] = None
    tags: List[str] = None
    metadata: Dict[str, Any] = None
    original_path: Optional[str] = None
    chunk_index: int = 0
    total_chunks: int = 1
    content_hash: Optional[str] = None
    embedding: Optional[np.ndarray] = None
    
    def __post_init__(self):
        if self.content_hash is None:
            self.content_hash = hashlib.md5(self.content.encode('utf-8')).hexdigest()
        if self.tags is None:
            self.tags = []
        if self.metadata is None:
            self.metadata = {}

class StructuredFolderProcessor:
    """Enhanced processor for structured Appcircle documentation folder"""
    
    def __init__(self, structured_folder_path: str):
        self.structured_folder_path = Path(structured_folder_path)
        self.processed_documents = []
        self.file_statistics = {
            'total_files': 0,
            'processed_files': 0,
            'failed_files': 0,
            'total_documents': 0,
            'sections': set()
        }
    
    def process_all_files(self) -> List[ProcessedDocument]:
        """Process all JSON files in the structured folder"""
        logger.info(f"Starting to process files in: {self.structured_folder_path}")
        
        if not self.structured_folder_path.exists():
            logger.error(f"Structured folder not found: {self.structured_folder_path}")
            return []
        
        # Find all JSON files recursively
        json_files = list(self.structured_folder_path.glob('**/*.json'))
        self.file_statistics['total_files'] = len(json_files)
        
        logger.info(f"Found {len(json_files)} JSON files to process")
        
        for json_file in json_files:
            try:
                self._process_single_file(json_file)
                self.file_statistics['processed_files'] += 1
            except Exception as e:
                logger.error(f"Failed to process {json_file}: {str(e)}")
                self.file_statistics['failed_files'] += 1
        
        self.file_statistics['total_documents'] = len(self.processed_documents)
        self._log_statistics()
        
        return self.processed_documents
    
    def _process_single_file(self, file_path: Path):
        """Process a single JSON file and extract documents"""
        logger.info(f"Processing: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Determine section from filename
        section = self._extract_section_from_filename(file_path.stem)
        self.file_statistics['sections'].add(section)
        
        # Handle different JSON structures
        documents = self._extract_documents_from_json(data, file_path, section)
        
        # Process each document for chunking and cleaning
        for doc_data in documents:
            processed_docs = self._process_document(doc_data, section)
            self.processed_documents.extend(processed_docs)
    
    def _extract_section_from_filename(self, filename: str) -> str:
        """Extract section name from filename"""
        # Map common filename patterns to sections
        section_mappings = {
            'build': 'Build & CI/CD',
            'environment': 'Environment Variables', 
            'workflows': 'Workflows',
            'self-hosted': 'Self-Hosted',
            'publish': 'Publishing',
            'marketplace': 'Marketplace',
            'api-cli': 'API & CLI',
            'misc': 'Miscellaneous'
        }
        
        for key, value in section_mappings.items():
            if key in filename.lower():
                return value
        
        return filename.replace('-', ' ').title()
    
    def _extract_documents_from_json(self, data: Dict, file_path: Path, section: str) -> List[Dict]:
        """Extract documents from various JSON structures"""
        documents = []
        
        if isinstance(data, dict):
            # Structure with 'documents' array (like build.json, marketplace.json)
            if 'documents' in data and isinstance(data['documents'], list):
                for doc in data['documents']:
                    if isinstance(doc, dict):
                        documents.append({
                            **doc,
                            'section': data.get('section_title', section),
                            'source_file': str(file_path)
                        })
            
            # Single document structure
            elif 'content' in data or 'title' in data:
                documents.append({
                    **data,
                    'section': section,
                    'source_file': str(file_path)
                })
            
            # Raw content structure (for misc files)
            else:
                # Create document from the entire JSON structure
                content = self._extract_content_from_dict(data)
                if content.strip():
                    documents.append({
                        'id': file_path.stem,
                        'title': section,
                        'content': content,
                        'section': section,
                        'source_file': str(file_path),
                        'raw_data': True
                    })
        
        return documents
    
    def _extract_content_from_dict(self, data: Dict) -> str:
        """Extract meaningful text content from a dictionary structure"""
        content_parts = []
        
        def extract_text(obj, depth=0):
            if depth > 10:  # Prevent infinite recursion
                return
            
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if isinstance(value, str) and len(value) > 20:
                        content_parts.append(f"{key}: {value}")
                    elif isinstance(value, (dict, list)):
                        extract_text(value, depth + 1)
            elif isinstance(obj, list):
                for item in obj:
                    extract_text(item, depth + 1)
            elif isinstance(obj, str) and len(obj) > 20:
                content_parts.append(obj)
        
        extract_text(data)
        return '\n\n'.join(content_parts)
    
    def _process_document(self, doc_data: Dict, section: str) -> List[ProcessedDocument]:
        """Process a single document, clean content, and create chunks"""
        content = str(doc_data.get('content', ''))
        
        # Clean the content
        cleaned_content = self._clean_content(content)
        
        if len(cleaned_content.strip()) < 50:  # Skip very short content
            return []
        
        # Create chunks if content is long
        chunks = self._create_content_chunks(cleaned_content, chunk_size=1500, overlap=300)
        
        processed_docs = []
        for i, chunk in enumerate(chunks):
            processed_doc = ProcessedDocument(
                id=f"{doc_data.get('id', 'unknown')}_{i}" if len(chunks) > 1 else doc_data.get('id', 'unknown'),
                title=doc_data.get('title', 'Untitled'),
                content=chunk,
                section=doc_data.get('section', section),
                description=doc_data.get('description'),
                url=doc_data.get('url'),
                tags=doc_data.get('tags', []),
                metadata={
                    'chunk_index': i,
                    'total_chunks': len(chunks),
                    'source_file': doc_data.get('source_file'),
                    'original_path': doc_data.get('original_path'),
                    'sidebar_position': doc_data.get('metadata', {}).get('sidebar_position'),
                    'raw_data': doc_data.get('raw_data', False)
                },
                original_path=doc_data.get('original_path'),
                chunk_index=i,
                total_chunks=len(chunks)
            )
            processed_docs.append(processed_doc)
        
        return processed_docs
    
    def _clean_content(self, content: str) -> str:
        """Comprehensive content cleaning for Appcircle documentation"""
        if not content:
            return ""
        
        # Remove import statements and component references
        content = re.sub(r'import.*?from.*?;', '', content)
        content = re.sub(r'<Screenshot.*?/>', '', content)
        content = re.sub(r'<.*?Ref.*?/>', '', content)
        
        # Clean markdown syntax
        content = re.sub(r'#{1,6}\s+', '', content)  # Headers
        content = re.sub(r'\*\*(.*?)\*\*', r'\1', content)  # Bold
        content = re.sub(r'\*(.*?)\*', r'\1', content)  # Italic
        content = re.sub(r'`([^`]+)`', r'\1', content)  # Inline code
        content = re.sub(r'```[\s\S]*?```', '', content)  # Code blocks
        content = re.sub(r'!\[.*?\]\(.*?\)', '', content)  # Images
        content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)  # Links (keep text)
        
        # Clean HTML-like tags
        content = re.sub(r'<[^>]+>', '', content)
        
        # Clean special markdown elements
        content = re.sub(r':::(.*?):::', '', content, flags=re.DOTALL)  # Admonitions
        content = re.sub(r'---[\s\S]*?---', '', content)  # Front matter
        
        # Normalize whitespace
        content = re.sub(r'\n\s*\n', '\n\n', content)
        content = re.sub(r'\s+', ' ', content)
        content = re.sub(r'\n\s+', '\n', content)
        
        # Remove table formatting
        content = re.sub(r'\|.*?\|', '', content)
        content = re.sub(r'\+-+\+', '', content)
        
        return content.strip()
    
    def _create_content_chunks(self, content: str, chunk_size: int = 1500, overlap: int = 300) -> List[str]:
        """Create overlapping chunks from content"""
        if len(content) <= chunk_size:
            return [content]
        
        words = content.split()
        chunks = []
        
        start = 0
        while start < len(words):
            end = min(start + chunk_size, len(words))
            chunk = ' '.join(words[start:end])
            
            if len(chunk.strip()) > 50:  # Only include substantial chunks
                chunks.append(chunk.strip())
            
            if end >= len(words):
                break
            
            start = end - overlap
        
        return chunks
    
    def _log_statistics(self):
        """Log processing statistics"""
        stats = self.file_statistics
        logger.info("Processing completed:")
        logger.info(f"  Total files found: {stats['total_files']}")
        logger.info(f"  Successfully processed: {stats['processed_files']}")
        logger.info(f"  Failed to process: {stats['failed_files']}")
        logger.info(f"  Total documents extracted: {stats['total_documents']}")
        logger.info(f"  Sections found: {sorted(stats['sections'])}")
    
    def export_processed_documents(self, output_path: str):
        """Export processed documents to JSON"""
        export_data = {
            'metadata': {
                'total_documents': len(self.processed_documents),
                'processing_statistics': dict(self.file_statistics),
                'sections': sorted(self.file_statistics['sections'])
            },
            'documents': [
                {
                    'id': doc.id,
                    'title': doc.title,
                    'content': doc.content,
                    'section': doc.section,
                    'description': doc.description,
                    'url': doc.url,
                    'tags': doc.tags,
                    'metadata': doc.metadata,
                    'original_path': doc.original_path,
                    'chunk_info': {
                        'index': doc.chunk_index,
                        'total': doc.total_chunks
                    }
                }
                for doc in self.processed_documents
            ]
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Exported {len(self.processed_documents)} documents to {output_path}")
    
    def get_documents_by_section(self, section: str) -> List[ProcessedDocument]:
        """Get all documents from a specific section"""
        return [doc for doc in self.processed_documents if doc.section == section]
    
    def get_processing_summary(self) -> Dict[str, Any]:
        """Get a summary of processing results"""
        sections_summary = {}
        for section in self.file_statistics['sections']:
            docs_in_section = self.get_documents_by_section(section)
            sections_summary[section] = len(docs_in_section)
        
        return {
            'total_documents': len(self.processed_documents),
            'total_files_processed': self.file_statistics['processed_files'],
            'sections': sections_summary,
            'average_content_length': sum(len(doc.content) for doc in self.processed_documents) / len(self.processed_documents) if self.processed_documents else 0
        }

class VectorDatabaseManager:
    """Manages vector embeddings and ChromaDB operations"""
    
    def __init__(self, db_path: str = "vector_db", model_name: str = "all-MiniLM-L6-v2"):
        self.db_path = db_path
        self.model_name = model_name
        self.model = None
        self.chroma_client = None
        self.collection = None
        
    def initialize(self):
        """Initialize embedding model and ChromaDB"""
        logger.info(f"Initializing embedding model: {self.model_name}")
        self.model = SentenceTransformer(self.model_name)
        
        logger.info(f"Initializing ChromaDB at: {self.db_path}")
        self.chroma_client = chromadb.PersistentClient(path=self.db_path)
        
        # Create or get collection
        self.collection = self.chroma_client.get_or_create_collection(
            name="appcircle_docs",
            metadata={"description": "Appcircle documentation embeddings"}
        )
        
        logger.info("Vector database initialized successfully")
    
    def generate_embeddings(self, documents: List[ProcessedDocument], batch_size: int = 32) -> List[ProcessedDocument]:
        """Generate embeddings for a list of documents"""
        if not self.model:
            raise ValueError("Model not initialized. Call initialize() first.")
        
        logger.info(f"Generating embeddings for {len(documents)} documents")
        
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i + batch_size]
            texts = [doc.content for doc in batch]
            
            try:
                embeddings = self.model.encode(texts, show_progress_bar=True)
                
                for j, embedding in enumerate(embeddings):
                    batch[j].embedding = embedding
                    
            except Exception as e:
                logger.error(f"Failed to generate embeddings for batch {i}: {str(e)}")
                continue
        
        embedded_count = sum(1 for doc in documents if doc.embedding is not None)
        logger.info(f"Successfully generated embeddings for {embedded_count}/{len(documents)} documents")
        
        return documents
    
    def store_in_vector_db(self, documents: List[ProcessedDocument]):
        """Store documents with embeddings in ChromaDB"""
        if not self.collection:
            raise ValueError("ChromaDB not initialized. Call initialize() first.")
        
        # Filter documents with embeddings
        docs_with_embeddings = [doc for doc in documents if doc.embedding is not None]
        
        if not docs_with_embeddings:
            logger.warning("No documents with embeddings found")
            return
        
        logger.info(f"Storing {len(docs_with_embeddings)} documents in vector database")
        
        # Prepare data for ChromaDB
        ids = [doc.id for doc in docs_with_embeddings]
        embeddings = [doc.embedding.tolist() for doc in docs_with_embeddings]
        documents = [doc.content for doc in docs_with_embeddings]
        metadatas = []
        
        for doc in docs_with_embeddings:
            metadata = {
                'title': doc.title,
                'section': doc.section,
                'url': doc.url or '',
                'description': doc.description or '',
                'tags': ','.join(doc.tags) if doc.tags else '',
                'chunk_index': doc.chunk_index,
                'total_chunks': doc.total_chunks,
                'content_hash': doc.content_hash,
                'original_path': doc.original_path or ''
            }
            # Add custom metadata
            if doc.metadata:
                for key, value in doc.metadata.items():
                    if isinstance(value, (str, int, float, bool)):
                        metadata[f'custom_{key}'] = str(value)
            
            metadatas.append(metadata)
        
        try:
            # Clear existing data (optional - remove if you want to append)
            # self.collection.delete()
            
            # Add documents to collection
            self.collection.add(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas
            )
            
            logger.info(f"Successfully stored {len(docs_with_embeddings)} documents in vector database")
            
        except Exception as e:
            logger.error(f"Failed to store documents in vector database: {str(e)}")
            raise
    
    def search_similar(self, query: str, n_results: int = 5, include_metadata: bool = True) -> Dict[str, Any]:
        """Search for similar documents"""
        if not self.collection or not self.model:
            raise ValueError("Vector database not initialized")
        
        # Generate query embedding
        query_embedding = self.model.encode([query])
        
        # Search in ChromaDB
        results = self.collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=n_results,
            include=['documents', 'metadatas', 'distances'] if include_metadata else ['documents', 'distances']
        )
        
        return results
    
    def get_collection_stats(self) -> Dict[str, Any]:
        """Get statistics about the vector database collection"""
        if not self.collection:
            return {}
        
        count = self.collection.count()
        return {
            'total_documents': count,
            'collection_name': self.collection.name,
            'embedding_model': self.model_name
        }

# Main processing function
def process_structured_folder(structured_folder_path: str, output_file: str = None) -> List[ProcessedDocument]:
    """
    Main function to process the structured folder
    
    Args:
        structured_folder_path: Path to the structured_folder directory
        output_file: Optional path to save processed documents as JSON
    
    Returns:
        List of ProcessedDocument objects
    """
    processor = StructuredFolderProcessor(structured_folder_path)
    processed_documents = processor.process_all_files()
    
    # Export if output file specified
    if output_file:
        processor.export_processed_documents(output_file)
    
    # Print summary
    summary = processor.get_processing_summary()
    print("\n" + "="*50)
    print("PROCESSING SUMMARY")
    print("="*50)
    print(f"Total documents processed: {summary['total_documents']}")
    print(f"Files processed: {summary['total_files_processed']}")
    print(f"Average content length: {summary['average_content_length']:.0f} characters")
    print("\nDocuments by section:")
    for section, count in summary['sections'].items():
        print(f"  {section}: {count} documents")
    
    return processed_documents

def create_vector_database(
    structured_folder_path: str = "structured_docs",
    vector_db_path: str = "vector_db",
    embedding_model: str = "all-MiniLM-L6-v2",
    output_json: str = None,
    clear_existing: bool = False
) -> Dict[str, Any]:
    """
    Complete pipeline to create vector database from structured docs
    
    Args:
        structured_folder_path: Path to structured docs folder
        vector_db_path: Path for ChromaDB storage
        embedding_model: Name of sentence transformer model
        output_json: Optional JSON export path
        clear_existing: Whether to clear existing vector database
        
    Returns:
        Dictionary with processing results and statistics
    """
    try:
        # Step 1: Process structured documents
        print("🔄 Step 1: Processing structured documents...")
        processor = StructuredFolderProcessor(structured_folder_path)
        documents = processor.process_all_files()
        
        if not documents:
            raise ValueError("No documents found to process")
        
        # Step 2: Initialize vector database manager
        print("🔄 Step 2: Initializing vector database...")
        vector_manager = VectorDatabaseManager(vector_db_path, embedding_model)
        vector_manager.initialize()
        
        # Step 3: Generate embeddings
        print("🔄 Step 3: Generating embeddings...")
        documents = vector_manager.generate_embeddings(documents)
        
        # Step 4: Store in vector database
        print("🔄 Step 4: Storing in vector database...")
        if clear_existing:
            print("  Clearing existing data...")
            try:
                vector_manager.collection.delete()
            except:
                pass
        
        vector_manager.store_in_vector_db(documents)
        
        # Step 5: Export JSON if requested
        if output_json:
            print(f"🔄 Step 5: Exporting to {output_json}...")
            processor.export_processed_documents(output_json)
        
        # Get final statistics
        processing_summary = processor.get_processing_summary()
        vector_stats = vector_manager.get_collection_stats()
        
        results = {
            'success': True,
            'documents_processed': len(documents),
            'documents_embedded': sum(1 for doc in documents if doc.embedding is not None),
            'processing_summary': processing_summary,
            'vector_database_stats': vector_stats,
            'vector_db_path': vector_db_path,
            'embedding_model': embedding_model
        }
        
        # Print final summary
        print("\n" + "="*60)
        print("🎉 VECTOR DATABASE CREATION COMPLETED!")
        print("="*60)
        print(f"✅ Total documents processed: {results['documents_processed']}")
        print(f"✅ Documents embedded: {results['documents_embedded']}")
        print(f"✅ Vector database location: {vector_db_path}")
        print(f"✅ Embedding model: {embedding_model}")
        print(f"✅ Collection size: {vector_stats.get('total_documents', 0)}")
        print("\nSection distribution:")
        for section, count in processing_summary['sections'].items():
            print(f"  📄 {section}: {count} documents")
        
        if output_json:
            print(f"✅ JSON export: {output_json}")
        
        print("\n🔍 Test your vector database:")
        print(f"  from preparedocsforvectordb import VectorDatabaseManager")
        print(f"  vm = VectorDatabaseManager('{vector_db_path}', '{embedding_model}')")
        print(f"  vm.initialize()")
        print(f"  results = vm.search_similar('your query here')")
        
        return results
        
    except Exception as e:
        logger.error(f"Vector database creation failed: {str(e)}")
        return {
            'success': False,
            'error': str(e),
            'documents_processed': 0,
            'documents_embedded': 0
        }

# Example usage
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Create vector database from Appcircle documentation")
    parser.add_argument("--structured-docs", default="structured_docs", 
                       help="Path to structured docs folder")
    parser.add_argument("--vector-db", default="vector_db", 
                       help="Path for vector database storage")
    parser.add_argument("--model", default="all-MiniLM-L6-v2", 
                       help="Embedding model name")
    parser.add_argument("--output-json", 
                       help="Optional JSON export path")
    parser.add_argument("--clear", action="store_true", 
                       help="Clear existing vector database")
    parser.add_argument("--test-query", 
                       help="Test query after creation")
    
    args = parser.parse_args()
    
    try:
        # Create vector database
        results = create_vector_database(
            structured_folder_path=args.structured_docs,
            vector_db_path=args.vector_db,
            embedding_model=args.model,
            output_json=args.output_json,
            clear_existing=args.clear
        )
        
        if results['success']:
            print(f"\n✅ Vector database created successfully!")
            
            # Test with query if provided
            if args.test_query:
                print(f"\n🔍 Testing with query: '{args.test_query}'")
                vector_manager = VectorDatabaseManager(args.vector_db, args.model)
                vector_manager.initialize()
                
                search_results = vector_manager.search_similar(args.test_query, n_results=3)
                
                print("Top 3 results:")
                for i, (doc, metadata, distance) in enumerate(zip(
                    search_results['documents'][0],
                    search_results['metadatas'][0], 
                    search_results['distances'][0]
                )):
                    print(f"\n{i+1}. {metadata.get('title', 'Unknown')} (score: {1-distance:.3f})")
                    print(f"   Section: {metadata.get('section', 'N/A')}")
                    print(f"   Preview: {doc[:150]}...")
        else:
            print(f"❌ Failed to create vector database: {results.get('error', 'Unknown error')}")
            
    except Exception as e:
        logger.error(f"Script execution failed: {e}")
        print(f"❌ Script failed: {e}")
        
    print("\n" + "="*60)
    print("📖 USAGE EXAMPLES:")
    print("="*60)
    print("# Basic usage:")
    print("python preparedocsforvectordb.py")
    print()
    print("# With custom paths:")
    print("python preparedocsforvectordb.py --structured-docs ./my_docs --vector-db ./my_vector_db")
    print()
    print("# Clear existing and test:")
    print("python preparedocsforvectordb.py --clear --test-query 'how to build iOS app'")
    print()
    print("# Export JSON:")
    print("python preparedocsforvectordb.py --output-json processed_docs.json")
    print()
    print("# Use different embedding model:")
    print("python preparedocsforvectordb.py --model all-mpnet-base-v2")