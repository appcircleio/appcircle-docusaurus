#!/usr/bin/env python3
"""
Contextual Search CLI - For semantic/contextual searches
Uses advanced vector search with term priority for understanding user intent
"""

import sys
import os
import re
from typing import List, Dict, Any
sys.path.append('/Users/ozer/Documents/codes/appcircle-docusaurus/pipeline/vector-database')

from test_user_term_priority import UserTermPriorityTester

class ContextualSearchEngine:
    """
    Contextual search engine for semantic queries and how-to questions
    """

    def __init__(self, db_path='vector_db', model='all-MiniLM-L6-v2'):
        self.tester = UserTermPriorityTester(db_path, model)

    def is_contextual_query(self, query: str) -> bool:
        """Determine if query is suitable for contextual search"""
        query_lower = query.lower()

        # Question patterns
        if any(query_lower.startswith(word) for word in ['how', 'what', 'why', 'when', 'where']):
            return True

        # Action patterns
        if any(word in query_lower for word in ['setup', 'configure', 'install', 'create', 'build']):
            return True

        # Guide/tutorial patterns
        if any(word in query_lower for word in ['guide', 'tutorial', 'example', 'best practice']):
            return True

        # Long descriptive queries (3+ words)
        if len(query.split()) >= 3:
            return True

        # Conceptual terms
        if any(word in query_lower for word in ['environment variables', 'ci cd', 'deployment', 'testing']):
            return True

        return False

    def contextual_search(self, query: str, n_results: int = 5) -> Dict[str, Any]:
        """
        Perform contextual search using the WINNING approach from benchmark:
        Exact-Term Prioritization (approach 3) - achieved 100% win rate
        """

        try:
            # Use the WINNING approach from benchmark: Exact-Term Prioritization
            result = self.tester.approach_3_exact_term_prioritization(query, n_results)

            # Format results for consistent interface
            formatted_results = []
            for res in result['results']:
                metadata = res['metadata']
                formatted_results.append({
                    'title': metadata.get('title', 'Unknown'),
                    'section': metadata.get('section', ''),
                    'url': metadata.get('url', ''),
                    'description': metadata.get('description', ''),
                    'priority_score': res['priority_score'],
                    'priority_explanation': res['priority_explanation'],
                    'term_coverage': res['term_coverage'],
                    'exact_matches': res['exact_matches'],
                    'semantic_score': res['semantic_score'],
                    'content_preview': res['content'][:200] + '...' if len(res['content']) > 200 else res['content']
                })

            return {
                'query': query,
                'search_type': 'contextual',
                'approach': 'Exact-Term Prioritization (Winner)',
                'user_terms': result['user_terms'],
                'results': formatted_results,
                'total': len(formatted_results),
                'message': f'Found {len(formatted_results)} contextual matches using winning approach'
            }

        except Exception as e:
            # Fallback to exact-term prioritization
            try:
                result = self.tester.approach_3_exact_term_prioritization(query, n_results)

                formatted_results = []
                for res in result['results']:
                    metadata = res['metadata']
                    formatted_results.append({
                        'title': metadata.get('title', 'Unknown'),
                        'section': metadata.get('section', ''),
                        'url': metadata.get('url', ''),
                        'description': metadata.get('description', ''),
                        'priority_score': res['priority_score'],
                        'priority_explanation': res['priority_explanation'],
                        'term_coverage': res['term_coverage'],
                        'exact_matches': res['exact_matches'],
                        'content_preview': res['content'][:200] + '...' if len(res['content']) > 200 else res['content']
                    })

                return {
                    'query': query,
                    'search_type': 'contextual',
                    'approach': 'Exact-Term Prioritization (fallback)',
                    'user_terms': result['user_terms'],
                    'results': formatted_results,
                    'total': len(formatted_results),
                    'message': f'Found {len(formatted_results)} matches using term prioritization'
                }

            except Exception as e2:
                return {
                    'query': query,
                    'search_type': 'contextual',
                    'results': [],
                    'total': 0,
                    'error': str(e2),
                    'message': 'Search failed'
                }

    def display_results(self, search_result: Dict[str, Any]) -> None:
        """Display contextual search results in a nice CLI format"""
        query = search_result['query']
        results = search_result['results']
        total = search_result['total']
        message = search_result['message']
        approach = search_result.get('approach', 'Unknown')
        user_terms = search_result.get('user_terms', [])

        print(f"\n🧠 CONTEXTUAL SEARCH (Semantic Understanding)")
        print("=" * 70)
        print(f"Query: '{query}'")
        print(f"User Terms: {', '.join(user_terms) if user_terms else 'None detected'}")
        print(f"Approach: {approach}")
        print(f"Results: {total} found")
        print(f"Info: {message}")
        print("-" * 70)

        if 'error' in search_result:
            print(f"❌ Error: {search_result['error']}")
            return

        if not results:
            print("❌ No contextual results found")
            print("\n💡 Suggestions:")
            print("   • Try rephrasing your question")
            print("   • Use more descriptive terms")
            print("   • Try exact term search for technical variables")
            return

        for i, result in enumerate(results, 1):
            title = result['title']
            section = result['section']
            url = result['url']

            print(f"\n🎯 #{i} {title}")
            print(f"    📁 Section: {section}")
            if url:
                print(f"    🔗 URL: {url}")

            # Show metrics for Exact-Term Prioritization approach
            if 'priority_score' in result:
                print(f"    🎯 Priority Score: {result['priority_score']:.3f}")
                print(f"    💡 {result['priority_explanation']}")
                print(f"    📊 Term Coverage: {result['term_coverage']:.1%}")
                if result['exact_matches']:
                    print(f"    ✅ Found Terms: {', '.join(result['exact_matches'])}")

            # Legacy support for other approaches
            elif 'user_friendly_response' in result:
                print(f"    🎭 Response: {result['user_friendly_response']}")
                print(f"    📊 Term Coverage: {result['term_coverage']:.1%}")
                print(f"    ✅ Contains User Terms: {result['contains_user_terms']}")

            print(f"    📄 Preview: {result['content_preview']}")

        print("\n" + "=" * 70)

def main():
    """CLI interface for contextual search testing"""
    print("🧠 Contextual Search CLI - Semantic Understanding")
    print("=" * 70)
    print("Designed for:")
    print("  • How-to questions (How to setup CI/CD?)")
    print("  • Conceptual queries (environment variables setup)")
    print("  • Best practices (iOS app signing best practices)")
    print("  • Guides and tutorials")
    print("  • Multi-word descriptive searches")
    print()
    print("Commands:")
    print("  search [query]  - Search contextually")
    print("  test           - Run test queries")
    print("  compare [query] - Compare all approaches")
    print("  help           - Show this help")
    print("  quit           - Exit")
    print("=" * 70)

    try:
        searcher = ContextualSearchEngine()
        stats = searcher.tester.vm.get_collection_stats()
        print(f"✅ Connected to vector database ({stats['total_documents']} documents)")
    except Exception as e:
        print(f"❌ Failed to initialize search: {e}")
        return

    while True:
        try:
            user_input = input("\n🧠 Contextual> ").strip()

            if not user_input or user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break

            if user_input.lower() == 'help':
                print("\n📚 Contextual Search Help:")
                print("  This tool uses semantic understanding for complex queries")
                print("  Best for: 'How to setup CI/CD', 'iOS deployment guide', etc.")
                print("  Example: search how to configure environment variables")
                continue

            if user_input.lower() == 'test':
                print("\n🧪 Running contextual test queries...")
                test_queries = [
                    "how to setup CI/CD pipeline",
                    "environment variables configuration",
                    "iOS app deployment best practices",
                    "configure build settings",
                    "setting up fastlane for automation",
                    "troubleshooting build failures",
                    "React Native testing setup"
                ]

                for query in test_queries:
                    print(f"\n--- Testing: '{query}' ---")
                    if searcher.is_contextual_query(query):
                        result = searcher.contextual_search(query, n_results=2)
                        searcher.display_results(result)
                    else:
                        print(f"❌ '{query}' should use exact term search instead")
                continue

            # Parse commands
            if user_input.startswith('search '):
                query = user_input[7:].strip()
                if not query:
                    print("❌ Please provide a query. Example: search how to setup CI/CD")
                    continue
            elif user_input.startswith('compare '):
                query = user_input[8:].strip()
                if not query:
                    print("❌ Please provide a query. Example: compare AC_PROJECT_PATH")
                    continue

                # Run comparison of all approaches
                print(f"\n🔬 Comparing all approaches for: '{query}'")
                try:
                    searcher.tester.compare_all_approaches(query)
                except Exception as e:
                    print(f"❌ Comparison failed: {e}")
                continue
            else:
                query = user_input

            # Check if query is suitable for contextual search
            if not searcher.is_contextual_query(query):
                print(f"⚠️  '{query}' seems like an exact term query")
                print("   Consider using algolia_search.py instead")
                print("   Proceeding with contextual search anyway...")

            # Perform search
            result = searcher.contextual_search(query)
            searcher.display_results(result)

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()