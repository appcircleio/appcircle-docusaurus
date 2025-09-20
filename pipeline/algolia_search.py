#!/usr/bin/env python3
"""
Algolia Search CLI - For exact term searches
Simulates the existing Algolia search functionality for technical terms
"""

import sys
import os
import re
import json
from typing import List, Dict, Any
sys.path.append('/Users/ozer/Documents/codes/appcircle-docusaurus/pipeline/vector-database')

from preparedocsforvectordb import VectorDatabaseManager

# Use HTTP approach since algoliasearch v4 API has different imports
import urllib.request
import urllib.parse
ALGOLIA_AVAILABLE = True

class RealAlgoliaSearch:
    """
    Real Algolia search using the production configuration
    """

    def __init__(self):
        # Production Algolia configuration
        self.app_id = "4U9FKQJ034"
        self.api_key = "b56a5dc4e52ec9e97ad93981cc668c4a"
        self.index_name = "appcircle"

    def search(self, query: str, n_results: int = 5) -> Dict[str, Any]:
        """Search using real Algolia API via HTTP"""
        try:
            # Algolia REST API endpoint
            url = f"https://{self.app_id}-dsn.algolia.net/1/indexes/{self.index_name}/query"

            # Search parameters
            search_data = {
                "query": query,
                "hitsPerPage": n_results,
                "attributesToRetrieve": ["title", "content", "url", "hierarchy"],
                "highlightPreTag": "<mark>",
                "highlightPostTag": "</mark>"
            }

            # Prepare request
            data = json.dumps(search_data).encode('utf-8')

            req = urllib.request.Request(
                url,
                data=data,
                headers={
                    'X-Algolia-Application-Id': self.app_id,
                    'X-Algolia-API-Key': self.api_key,
                    'Content-Type': 'application/json'
                },
                method='POST'
            )

            # Make request
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode('utf-8'))

            # Format results
            formatted_results = []
            for hit in result.get('hits', []):
                content = hit.get('content') or ''
                formatted_results.append({
                    'title': hit.get('title', 'Unknown'),
                    'section': self._extract_section(hit.get('hierarchy', {})),
                    'url': hit.get('url', ''),
                    'description': content[:200] + '...' if len(content) > 200 else content,
                    'content_preview': content[:300] + '...' if len(content) > 300 else content,
                    'match_type': 'exact' if query.upper() in content.upper() else 'partial',
                    'algolia_score': hit.get('_rankingInfo', {}).get('totalRankingScore', 0),
                    'highlighted': hit.get('_highlightResult', {}),
                    'metadata': hit
                })

            return {
                'query': query,
                'search_type': 'exact_term',
                'results': formatted_results,
                'total': result.get('nbHits', 0),
                'message': f'Found {len(formatted_results)} results via Algolia HTTP API',
                'algolia_processing_time': result.get('processingTimeMS', 0)
            }

        except Exception as e:
            return {
                'query': query,
                'search_type': 'exact_term',
                'results': [],
                'total': 0,
                'error': str(e),
                'message': 'Algolia HTTP search failed'
            }

    def _extract_section(self, hierarchy: Dict) -> str:
        """Extract section name from Algolia hierarchy"""
        if not hierarchy:
            return 'Unknown'

        # Try to get the most specific hierarchy level
        for level in ['lvl3', 'lvl2', 'lvl1', 'lvl0']:
            if hierarchy.get(level):
                return hierarchy[level]

        return 'Unknown'

class AlgoliaSearchSimulator:
    """
    Algolia search with fallback to vector simulation
    Uses real Algolia API when available, falls back to vector search simulation
    """

    def __init__(self, use_real_algolia=True, db_path='vector-database/vector_db', model='all-MiniLM-L6-v2'):
        self.use_real_algolia = use_real_algolia and ALGOLIA_AVAILABLE

        if self.use_real_algolia:
            try:
                self.algolia = RealAlgoliaSearch()
                print("✅ Connected to real Algolia API")
            except Exception as e:
                print(f"⚠️  Failed to connect to Algolia API: {e}")
                print("📄 Falling back to vector simulation")
                self.use_real_algolia = False

        if not self.use_real_algolia:
            self.vm = VectorDatabaseManager(db_path, model)
            self.vm.initialize()
            print("✅ Using vector database simulation")

    def is_exact_term_query(self, query: str) -> bool:
        """Determine if query is suitable for exact term search"""
        query = query.strip()

        # Technical variable patterns
        if re.match(r'^[A-Z_]+$', query):  # AC_PROJECT_PATH
            return True

        # Error message patterns
        if re.search(r'[A-Z_]+ (not found|missing|error|undefined)', query, re.IGNORECASE):
            return True

        # Short exact phrases (2 words or less, no question words)
        words = query.split()
        if len(words) <= 2 and not any(w.lower() in ['how', 'what', 'why', 'when', 'where'] for w in words):
            return True

        # API/service names
        if query.lower() in ['fastlane', 'cocoapods', 'gradle', 'xcode', 'carthage']:
            return True

        return False

    def exact_term_search(self, query: str, n_results: int = 5) -> Dict[str, Any]:
        """
        Perform exact term search using real Algolia API or vector simulation
        """

        if self.use_real_algolia:
            # Use real Algolia API
            return self.algolia.search(query, n_results)

        # Fallback to vector simulation
        results = self.vm.search_similar(query, n_results=n_results * 3)

        if not results['documents'] or not results['documents'][0]:
            return {
                'query': query,
                'search_type': 'exact_term',
                'results': [],
                'total': 0,
                'message': 'No exact matches found'
            }

        # Prioritize exact matches
        exact_matches = []
        partial_matches = []

        for doc, metadata, distance in zip(
            results['documents'][0],
            results['metadatas'][0],
            results['distances'][0]
        ):
            title = metadata.get('title', '')
            content = doc

            # Check for exact term in content
            query_upper = query.upper()
            has_exact_match = query_upper in content.upper() or query_upper in title.upper()

            result_item = {
                'title': title,
                'section': metadata.get('section', ''),
                'url': metadata.get('url', ''),
                'description': metadata.get('description', ''),
                'content_preview': content[:200] + '...' if len(content) > 200 else content,
                'match_type': 'exact' if has_exact_match else 'partial',
                'similarity_score': 1 - distance,
                'metadata': metadata
            }

            if has_exact_match:
                exact_matches.append(result_item)
            else:
                partial_matches.append(result_item)

        # Combine results: exact matches first, then partial
        final_results = exact_matches + partial_matches
        final_results = final_results[:n_results]

        return {
            'query': query,
            'search_type': 'exact_term',
            'results': final_results,
            'total': len(final_results),
            'exact_matches': len(exact_matches),
            'message': f'Found {len(exact_matches)} exact matches, {len(partial_matches)} related results'
        }

    def display_results(self, search_result: Dict[str, Any]) -> None:
        """Display search results in a nice CLI format"""
        query = search_result['query']
        results = search_result['results']
        total = search_result['total']
        message = search_result['message']

        print(f"\n🔍 ALGOLIA SEARCH (Exact Term)")
        print("=" * 60)
        print(f"Query: '{query}'")
        print(f"Results: {total} found")
        print(f"Info: {message}")
        print("-" * 60)

        if not results:
            print("❌ No results found")
            print("\n💡 Suggestions:")
            print("   • Check spelling of technical terms")
            print("   • Try the contextual search for broader results")
            print("   • Use exact variable names (e.g., AC_PROJECT_PATH)")
            return

        for i, result in enumerate(results, 1):
            title = result['title']
            section = result['section']
            url = result['url']
            match_type = result['match_type']
            preview = result['content_preview']

            match_icon = "✅" if match_type == 'exact' else "🔗"

            print(f"\n{match_icon} #{i} {title}")
            print(f"    📁 Section: {section}")
            if url:
                print(f"    🔗 URL: {url}")
            print(f"    🎯 Match: {match_type.title()}")
            print(f"    📄 Preview: {preview}")

            # Highlight the search term in preview
            if query.upper() in preview.upper():
                print(f"    ✨ Contains: '{query}'")

        print("\n" + "=" * 60)

def main():
    """CLI interface for Algolia search testing"""
    print("🔍 Algolia Search CLI - Exact Term Matching")
    print("=" * 60)
    print("Designed for:")
    print("  • Technical variables (AC_PROJECT_PATH, FASTLANE_PASSWORD)")
    print("  • Error messages (AC_PROJECT_PATH not found)")
    print("  • API/tool names (fastlane, gradle)")
    print("  • Short exact phrases")
    print()
    print("Commands:")
    print("  search [query]  - Search for exact terms")
    print("  test           - Run test queries")
    print("  help           - Show this help")
    print("  quit           - Exit")
    print("=" * 60)

    try:
        searcher = AlgoliaSearchSimulator()
        if searcher.use_real_algolia:
            print("✅ Using real Algolia API")
        else:
            stats = searcher.vm.get_collection_stats()
            print(f"✅ Connected to vector database ({stats['total_documents']} documents)")
    except Exception as e:
        print(f"❌ Failed to initialize search: {e}")
        return

    while True:
        try:
            user_input = input("\n🎯 Algolia> ").strip()

            if not user_input or user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break

            if user_input.lower() == 'help':
                print("\n📚 Algolia Search Help:")
                print("  This tool simulates Algolia's exact term matching")
                print("  Best for: AC_PROJECT_PATH, fastlane, gradle, etc.")
                print("  Example: search AC_PROJECT_PATH")
                continue

            if user_input.lower() == 'test':
                print("\n🧪 Running test queries...")
                test_queries = [
                    "AC_PROJECT_PATH",
                    "FASTLANE_PASSWORD",
                    "AC_PROJECT_PATH not found",
                    "fastlane",
                    "gradle",
                    "PAT"
                ]

                for query in test_queries:
                    print(f"\n--- Testing: '{query}' ---")
                    if searcher.is_exact_term_query(query):
                        result = searcher.exact_term_search(query, n_results=2)
                        searcher.display_results(result)
                    else:
                        print(f"❌ '{query}' should use contextual search instead")
                continue

            # Parse search command
            if user_input.startswith('search '):
                query = user_input[7:].strip()
                if not query:
                    print("❌ Please provide a query. Example: search AC_PROJECT_PATH")
                    continue
            else:
                query = user_input

            # Check if query is suitable for exact search
            if not searcher.is_exact_term_query(query):
                print(f"⚠️  '{query}' seems like a contextual query")
                print("   Consider using contextual_search.py instead")
                print("   Proceeding with exact search anyway...")

            # Perform search
            result = searcher.exact_term_search(query)
            searcher.display_results(result)

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()