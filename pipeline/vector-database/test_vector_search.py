#!/usr/bin/env python3
"""
Interactive Vector Database Search Tool
Run queries against your Appcircle documentation vector database
"""

import sys
from preparedocsforvectordb import VectorDatabaseManager

def main():
    print("🔍 Appcircle Documentation Vector Search")
    print("=" * 50)
    
    # Initialize vector database
    try:
        vm = VectorDatabaseManager('vector_db', 'all-MiniLM-L6-v2')
        vm.initialize()
        stats = vm.get_collection_stats()
        print(f"✅ Connected to vector database ({stats['total_documents']} documents)")
        print()
    except Exception as e:
        print(f"❌ Failed to connect to vector database: {e}")
        print("Make sure you've run the vector database creation script first.")
        return
    
    print("Enter your queries (type 'quit' to exit, 'help' for commands):")
    print("💡 Tip: Add --full to see complete content, --preview for summary")
    print("-" * 50)
    
    while True:
        try:
            query = input("\n🔍 Query: ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if query.lower() == 'help':
                print_help()
                continue
            
            if query.lower() == 'stats':
                print_stats(vm)
                continue
            
            if not query:
                continue
            
            # Check for display options
            show_full = False
            show_preview = False
            
            if '--full' in query:
                show_full = True
                query = query.replace('--full', '').strip()
            else:
                show_preview = True
                query = query.replace('--preview', '').strip()

            # Process query
            print(f"\n🔄 Searching for: '{query}'")
            results = vm.search_similar(query, n_results=3)
            
            print("\n📝 Results:")
            print("-" * 40)
            
            for i, (doc, metadata, distance) in enumerate(zip(
                results['documents'][0],
                results['metadatas'][0], 
                results['distances'][0]
            )):
                similarity = 1 - distance
                print(f"\n{i+1}. 📄 {metadata.get('title', 'Unknown')}")
                print(f"   📊 Similarity: {similarity:.3f}")
                print(f"   📁 Section: {metadata.get('section', 'N/A')}")
                if metadata.get('url'):
                    print(f"   🔗 URL: {metadata.get('url')}")
                # Display content based on user preference
                if show_preview:
                    print(f"   📖 Preview: {doc[:300]}...")
                else:  # show_full
                    print(f"   📖 Full Content:")
                    # Indent each line for better readability
                    content_lines = doc.split('\n')
                    for line in content_lines:
                        print(f"      {line}")
                
                print("   " + "-" * 60)
                
                if similarity > 0.7:
                    print("   ⭐ High relevance match!")
                elif similarity > 0.4:
                    print("   ✅ Good match")
                elif similarity > 0.2:
                    print("   🔸 Moderate match")
                else:
                    print("   🔹 Low relevance")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error processing query: {e}")

def print_help():
    print("\n📚 Available commands:")
    print("  help  - Show this help message")
    print("  stats - Show database statistics")
    print("  quit  - Exit the program")
    print("\n💡 Example queries:")
    print("  'how to build iOS app'")
    print("  'environment variables --preview'")
    print("  'code signing certificates --full'")
    print("  'testing mobile applications'")
    print("  'publish to app store'")
    print("\n🔧 Display options:")
    print("  --full    Show complete document content (default)")
    print("  --preview Show first 300 characters only")

def print_stats(vm):
    stats = vm.get_collection_stats()
    collection_info = vm.collection.get()
    metadatas = collection_info['metadatas']
    
    print(f"\n📊 Database Statistics:")
    print(f"  Total documents: {stats['total_documents']}")
    print(f"  Embedding model: {stats['embedding_model']}")
    
    # Count by section
    sections = {}
    for metadata in metadatas:
        section = metadata.get('section', 'Unknown')
        sections[section] = sections.get(section, 0) + 1
    
    print(f"\n📁 Documents by section:")
    for section, count in sorted(sections.items()):
        print(f"  {section}: {count}")

if __name__ == "__main__":
    main()