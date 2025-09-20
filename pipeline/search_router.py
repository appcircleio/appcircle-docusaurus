#!/usr/bin/env python3
"""
Search Router CLI - Demonstrates hybrid approach
Routes queries to appropriate search engine based on query classification
"""

import sys
import os
import re
from algolia_search import AlgoliaSearchSimulator
from contextual_search import ContextualSearchEngine

class SearchRouter:
    """
    Routes queries between exact term search (Algolia) and contextual search (Vector)
    """

    def __init__(self):
        print("🔄 Initializing search engines...")
        try:
            self.algolia = AlgoliaSearchSimulator()
            self.contextual = ContextualSearchEngine()
            print("✅ Both search engines initialized successfully")
        except Exception as e:
            print(f"❌ Failed to initialize search engines: {e}")
            raise

    def classify_query(self, query: str) -> str:
        """
        Classify query as 'exact' or 'contextual'
        This logic would be in the frontend in production
        """
        query = query.strip()

        # Check for exact term patterns first
        if self.algolia.is_exact_term_query(query):
            return 'exact'

        # Check for contextual patterns
        if self.contextual.is_contextual_query(query):
            return 'contextual'

        # Default fallback logic
        words = query.split()
        if len(words) <= 2:
            return 'exact'  # Short queries go to exact search
        else:
            return 'contextual'  # Longer queries go to contextual

    def route_search(self, query: str, n_results: int = 5):
        """
        Route query to appropriate search engine and return unified results
        """
        classification = self.classify_query(query)

        print(f"🎯 Query Classification: {classification.upper()}")
        print(f"📍 Routing to: {'Algolia (Exact Term)' if classification == 'exact' else 'Vector (Contextual)'}")

        if classification == 'exact':
            return self.algolia.exact_term_search(query, n_results)
        else:
            return self.contextual.contextual_search(query, n_results)

    def display_routing_info(self, query: str):
        """Show how the query would be classified and routed"""
        classification = self.classify_query(query)

        print(f"\n🔍 Query Analysis: '{query}'")
        print("-" * 50)
        print(f"📊 Classification: {classification.upper()}")

        if classification == 'exact':
            print("🎯 Route: Algolia Search (Exact Term)")
            print("📝 Reason: ", end="")
            if re.match(r'^[A-Z_]+$', query):
                print("Technical variable pattern")
            elif len(query.split()) <= 2:
                print("Short exact phrase")
            elif any(word in query.lower() for word in ['fastlane', 'gradle', 'xcode']):
                print("API/tool name")
            else:
                print("Exact term heuristics")
        else:
            print("🧠 Route: Vector Search (Contextual)")
            print("📝 Reason: ", end="")
            if any(query.lower().startswith(w) for w in ['how', 'what', 'why']):
                print("Question pattern")
            elif any(w in query.lower() for w in ['setup', 'configure', 'guide']):
                print("Action/guide pattern")
            elif len(query.split()) >= 3:
                print("Multi-word descriptive query")
            else:
                print("Contextual heuristics")

        print("-" * 50)

def main():
    """CLI interface for testing the hybrid search approach"""
    print("🚀 HYBRID SEARCH ROUTER")
    print("=" * 70)
    print("Demonstrates intelligent routing between two search approaches:")
    print("  🔍 Algolia Search  → Exact terms (AC_PROJECT_PATH, fastlane)")
    print("  🧠 Vector Search   → Contextual queries (how to setup CI/CD)")
    print()
    print("Commands:")
    print("  search [query]    - Smart search with automatic routing")
    print("  route [query]     - Show routing decision without searching")
    print("  exact [query]     - Force exact term search")
    print("  contextual [query] - Force contextual search")
    print("  test              - Run comparison tests")
    print("  help              - Show this help")
    print("  quit              - Exit")
    print("=" * 70)

    try:
        router = SearchRouter()
    except Exception as e:
        print(f"❌ Failed to initialize router: {e}")
        return

    while True:
        try:
            user_input = input("\n🚀 Router> ").strip()

            if not user_input or user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break

            if user_input.lower() == 'help':
                print("\n📚 Hybrid Search Help:")
                print("  This router automatically chooses the best search approach")
                print("  Examples:")
                print("    search AC_PROJECT_PATH           → Exact search")
                print("    search how to setup CI/CD        → Contextual search")
                print("    route AC_PROJECT_PATH            → Show routing decision")
                continue

            if user_input.lower() == 'test':
                print("\n🧪 Running hybrid search tests...")

                test_cases = [
                    ("AC_PROJECT_PATH", "exact"),
                    ("FASTLANE_PASSWORD", "exact"),
                    ("how to setup CI/CD", "contextual"),
                    ("environment variables guide", "contextual"),
                    ("fastlane", "exact"),
                    ("iOS deployment best practices", "contextual"),
                    ("PAT setup", "exact"),
                    ("configure build settings", "contextual")
                ]

                for query, expected in test_cases:
                    actual = router.classify_query(query)
                    result = "✅" if actual == expected else "❌"
                    print(f"{result} '{query}' → {actual} (expected: {expected})")

                continue

            # Parse commands
            command_parts = user_input.split(' ', 1)
            command = command_parts[0].lower()
            query = command_parts[1].strip() if len(command_parts) > 1 else ""

            if command == 'search':
                if not query:
                    print("❌ Please provide a query. Example: search AC_PROJECT_PATH")
                    continue

                result = router.route_search(query)

                if result['search_type'] == 'exact_term':
                    router.algolia.display_results(result)
                else:
                    router.contextual.display_results(result)

            elif command == 'route':
                if not query:
                    print("❌ Please provide a query. Example: route AC_PROJECT_PATH")
                    continue

                router.display_routing_info(query)

            elif command == 'exact':
                if not query:
                    print("❌ Please provide a query. Example: exact AC_PROJECT_PATH")
                    continue

                print("🔍 Forcing Algolia Search (Exact Term)")
                result = router.algolia.exact_term_search(query)
                router.algolia.display_results(result)

            elif command == 'contextual':
                if not query:
                    print("❌ Please provide a query. Example: contextual how to setup CI/CD")
                    continue

                print("🧠 Forcing Vector Search (Contextual)")
                result = router.contextual.contextual_search(query)
                router.contextual.display_results(result)

            else:
                # Default behavior - treat as search
                query = user_input
                result = router.route_search(query)

                if result['search_type'] == 'exact_term':
                    router.algolia.display_results(result)
                else:
                    router.contextual.display_results(result)

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()