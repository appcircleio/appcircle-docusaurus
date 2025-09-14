#!/usr/bin/env python3
"""
User Term Priority Testing Tool
Compare different approaches to prioritize user's exact terminology in search results

The core problem: Users search for "PAT setup" but get results about "Personal Access Token configuration"
Users think it's different content because terminology doesn't match their words.

This tool tests 3 approaches to solve term alignment issues:
1. Term-boosted vector search - Combine semantic similarity with exact term matching
2. User-terminology templates - Generate responses using user's exact words  
3. Exact-term prioritization - Heavily prioritize results containing user's terms
"""

import re
from typing import List, Dict, Any
from preparedocsforvectordb import VectorDatabaseManager

class UserTermPriorityTester:
    def __init__(self, db_path='vector_db', model='all-MiniLM-L6-v2'):
        self.vm = VectorDatabaseManager(db_path, model)
        self.vm.initialize()
        
    def extract_user_terms(self, query: str) -> List[str]:
        """Extract important terms from user query, preserving their exact words"""
        # Keep user's original terms but remove common stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'how', 'what', 'when', 'where', 'why', 'is', 'are', 'was', 'were', 'do', 'does', 'did'}
        
        # Preserve original case for terms like PAT, iOS, CI
        original_words = re.findall(r'\b\w+\b', query)
        user_terms = [word for word in original_words if word.lower() not in stop_words]
        
        return user_terms

    def calculate_exact_term_coverage(self, content: str, user_terms: List[str]) -> Dict[str, Any]:
        """Calculate how well content matches user's exact terms"""
        content_lower = content.lower()
        
        exact_matches = []
        for term in user_terms:
            if term.lower() in content_lower:
                exact_matches.append(term)
        
        coverage_ratio = len(exact_matches) / len(user_terms) if user_terms else 0
        
        return {
            'exact_matches': exact_matches,
            'missing_terms': [term for term in user_terms if term not in exact_matches],
            'coverage_ratio': coverage_ratio,
            'match_count': len(exact_matches)
        }

    def approach_1_term_boosted_search(self, query: str, n_results: int = 5) -> Dict[str, Any]:
        """
        Approach 1: Term-Boosted Vector Search
        Problem: Semantic search might find relevant content but miss user's exact terms
        Solution: Combine semantic similarity (60%) with exact term matching (40%)
        """
        user_terms = self.extract_user_terms(query)
        
        # Get broader results for reranking
        results = self.vm.search_similar(query, n_results=n_results * 2)
        
        boosted_results = []
        
        for doc, metadata, distance in zip(
            results['documents'][0],
            results['metadatas'][0], 
            results['distances'][0]
        ):
            # Skip release notes - they don't provide implementation guidance
            title = metadata.get('title', '').lower()
            if 'release notes' in title or 'latest release' in title:
                continue
                
            semantic_score = 1 - distance
            term_analysis = self.calculate_exact_term_coverage(doc, user_terms)
            
            # Boost score based on exact term matches
            term_boost = term_analysis['coverage_ratio'] * 0.4
            combined_score = (semantic_score * 0.6) + term_boost
            
            boosted_results.append({
                'content': doc,
                'metadata': metadata,
                'semantic_score': semantic_score,
                'term_coverage': term_analysis['coverage_ratio'],
                'exact_matches': term_analysis['exact_matches'],
                'missing_terms': term_analysis['missing_terms'],
                'combined_score': combined_score,
                'boost_amount': term_boost
            })
        
        # Sort by combined score (semantic + term boost)
        boosted_results.sort(key=lambda x: x['combined_score'], reverse=True)
        
        return {
            'query': query,
            'user_terms': user_terms,
            'results': boosted_results[:n_results],
            'approach': 'Term-Boosted Vector Search'
        }

    def approach_2_user_terminology_templates(self, query: str, n_results: int = 3) -> Dict[str, Any]:
        """
        Approach 2: User-Terminology Templates  
        Problem: System responds with different terminology than user used
        Solution: Generate responses that echo back user's exact terms
        """
        user_terms = self.extract_user_terms(query)
        results = self.vm.search_similar(query, n_results=n_results)
        
        template_responses = []
        
        for doc, metadata, distance in zip(
            results['documents'][0],
            results['metadatas'][0], 
            results['distances'][0]
        ):
            # Skip release notes - they don't provide implementation guidance
            title = metadata.get('title', '').lower()
            if 'release notes' in title or 'latest release' in title:
                continue
                
            semantic_score = 1 - distance
            term_analysis = self.calculate_exact_term_coverage(doc, user_terms)
            
            # Create response template using user's exact terms
            primary_user_term = user_terms[0] if user_terms else "your request"
            
            # Choose template based on query pattern
            if any(word in query.lower() for word in ['how', 'setup', 'create', 'configure', 'build']):
                if term_analysis['exact_matches']:
                    template = f"To {query.lower()}, here's the {primary_user_term} information:"
                else:
                    template = f"For {primary_user_term} setup, here's what you need:"
            elif any(word in query.lower() for word in ['what', 'explain', 'about']):
                template = f"About {primary_user_term}:"
            else:
                template = f"Regarding {primary_user_term}:"
            
            # Find the most relevant sentence that contains user terms if possible
            sentences = [s.strip() + '.' for s in doc.split('.') if s.strip()]
            
            # Prioritize sentences containing user terms
            best_sentence = ""
            for sentence in sentences:
                sentence_analysis = self.calculate_exact_term_coverage(sentence, user_terms)
                if sentence_analysis['match_count'] > 0:
                    best_sentence = sentence
                    break
            
            if not best_sentence and sentences:
                best_sentence = sentences[0]
            
            user_friendly_response = f"{template} {best_sentence}"
            
            template_responses.append({
                'user_friendly_response': user_friendly_response,
                'original_content': doc,
                'metadata': metadata,
                'semantic_score': semantic_score,
                'term_coverage': term_analysis['coverage_ratio'],
                'used_user_term': primary_user_term,
                'contains_user_terms': len(term_analysis['exact_matches']) > 0
            })
        
        return {
            'query': query,
            'user_terms': user_terms,
            'results': template_responses,
            'approach': 'User-Terminology Templates'
        }

    def approach_3_exact_term_prioritization(self, query: str, n_results: int = 3) -> Dict[str, Any]:
        """
        Approach 3: Exact-Term Prioritization
        Problem: Relevant content gets buried because it doesn't contain user's exact words
        Solution: Heavily prioritize results that contain user's exact terms
        """
        user_terms = self.extract_user_terms(query)
        
        # Get more results for better prioritization
        results = self.vm.search_similar(query, n_results=n_results * 4)
        
        prioritized_results = []
        
        for doc, metadata, distance in zip(
            results['documents'][0],
            results['metadatas'][0], 
            results['distances'][0]
        ):
            # Skip release notes - they don't provide implementation guidance
            title = metadata.get('title', '').lower()
            if 'release notes' in title or 'latest release' in title:
                continue
                
            semantic_score = 1 - distance
            term_analysis = self.calculate_exact_term_coverage(doc, user_terms)
            
            # Calculate priority score with heavy term weighting
            base_score = semantic_score * 0.3  # Semantic matters less
            
            # Big bonuses for exact term matches
            exact_term_bonus = term_analysis['match_count'] * 0.25  # 0.25 per matching term
            coverage_bonus = term_analysis['coverage_ratio'] * 0.3  # Bonus for term coverage
            
            # Extra bonus if all user terms are found
            perfect_match_bonus = 0.2 if term_analysis['coverage_ratio'] == 1.0 else 0
            
            # Check for phrase matching (user's terms appearing together)
            phrase_bonus = 0
            if len(user_terms) > 1:
                user_phrase = ' '.join(user_terms).lower()
                if user_phrase in doc.lower():
                    phrase_bonus = 0.3
            
            priority_score = base_score + exact_term_bonus + coverage_bonus + perfect_match_bonus + phrase_bonus
            
            prioritized_results.append({
                'content': doc,
                'metadata': metadata,
                'semantic_score': semantic_score,
                'term_coverage': term_analysis['coverage_ratio'],
                'exact_matches': term_analysis['exact_matches'],
                'missing_terms': term_analysis['missing_terms'],
                'exact_term_bonus': exact_term_bonus,
                'coverage_bonus': coverage_bonus,
                'perfect_match_bonus': perfect_match_bonus,
                'phrase_bonus': phrase_bonus,
                'priority_score': priority_score,
                'priority_explanation': self._explain_prioritization(term_analysis, phrase_bonus > 0)
            })
        
        # Sort by priority score (exact terms heavily weighted)
        prioritized_results.sort(key=lambda x: x['priority_score'], reverse=True)
        
        return {
            'query': query,
            'user_terms': user_terms,
            'results': prioritized_results[:n_results],
            'approach': 'Exact-Term Prioritization'
        }

    def _explain_prioritization(self, term_analysis: Dict, has_phrase_match: bool) -> str:
        """Explain why this result was prioritized"""
        if has_phrase_match:
            return "🎯 PERFECT: Contains your exact phrase"
        elif term_analysis['coverage_ratio'] == 1.0:
            return "⭐ EXCELLENT: Contains all your terms"
        elif term_analysis['match_count'] > 0:
            return f"✅ GOOD: Contains {term_analysis['match_count']}/{len(term_analysis['exact_matches']) + len(term_analysis['missing_terms'])} of your terms"
        else:
            return "🔄 SEMANTIC: Similar meaning, different words"

    def compare_all_approaches(self, query: str) -> None:
        """Test all three approaches and show detailed comparison"""
        print(f"\n{'='*90}")
        print(f"🔬 USER TERM PRIORITY COMPARISON: '{query}'")
        print(f"{'='*90}")
        
        # Extract user terms once
        user_terms = self.extract_user_terms(query)
        print(f"👤 User's Terms: {', '.join(user_terms)}")
        print(f"🎯 Goal: Find results that use these exact terms")
        
        approaches = [
            (self.approach_1_term_boosted_search, "Term-Boosted Vector Search"),
            (self.approach_2_user_terminology_templates, "User-Terminology Templates"), 
            (self.approach_3_exact_term_prioritization, "Exact-Term Prioritization")
        ]
        
        all_results = []
        
        for approach_func, approach_name in approaches:
            try:
                print(f"\n{'-'*60}")
                print(f"🧪 Testing: {approach_name}")
                print(f"{'-'*60}")
                
                result = approach_func(query, n_results=3)
                all_results.append(result)
                self._display_approach_results(result)
                
            except Exception as e:
                print(f"❌ Error in {approach_name}: {e}")
        
        # Show winner analysis
        self._display_winner_analysis(all_results, user_terms)

    def _display_approach_results(self, result: Dict[str, Any]) -> None:
        """Display results for a single approach"""
        approach = result['approach']
        
        for i, res in enumerate(result['results'][:2]):  # Show top 2 results
            metadata = res.get('metadata', {})
            title = metadata.get('title', 'Unknown Document')
            description = metadata.get('description', '')
            url = metadata.get('url', '')
            section = metadata.get('section', '')
            
            print(f"\n#{i+1} 📄 {title}")
            if description:
                print(f"   📝 Description: {description}")
            if section:
                print(f"   📁 Section: {section}")
            if url:
                print(f"   🔗 More details: {url}")
            
            if approach == 'Term-Boosted Vector Search':
                print(f"   🧠 Semantic: {res['semantic_score']:.3f}")
                print(f"   🎯 Term Coverage: {res['term_coverage']:.1%} ({len(res['exact_matches'])}/{len(result['user_terms'])} terms)")
                print(f"   ⚡ Combined Score: {res['combined_score']:.3f} (boost: +{res['boost_amount']:.3f})")
                print(f"   ✅ Found: {', '.join(res['exact_matches']) if res['exact_matches'] else 'None'}")
                print(f"   ❌ Missing: {', '.join(res['missing_terms']) if res['missing_terms'] else 'None'}")
                
            elif approach == 'User-Terminology Templates':
                print(f"   🧠 Semantic: {res['semantic_score']:.3f}")
                print(f"   🎯 Term Coverage: {res['term_coverage']:.1%}")
                print(f"   🏷️ Using User Term: '{res['used_user_term']}'")
                print(f"   📝 Response: {res['user_friendly_response']}")
                
            elif approach == 'Exact-Term Prioritization':
                print(f"   🧠 Semantic: {res['semantic_score']:.3f} (30% weight)")
                print(f"   🎯 Term Bonus: +{res['exact_term_bonus']:.3f}")
                print(f"   📊 Coverage Bonus: +{res['coverage_bonus']:.3f}")
                print(f"   🏆 Priority Score: {res['priority_score']:.3f}")
                print(f"   💡 {res['priority_explanation']}")
                
            # Show content preview for all approaches
            print(f"   📄 Content Preview: {res['content'][:200]}...")
            print("   " + "-" * 70)

    def _display_winner_analysis(self, all_results: List[Dict], user_terms: List[str]) -> None:
        """Analyze which approach performed best for user term alignment"""
        if not all_results:
            return
            
        print(f"\n{'='*60}")
        print("🏆 WINNER ANALYSIS - User Term Alignment")
        print(f"{'='*60}")
        
        query = all_results[0]['query']
        print(f"Query: '{query}'")
        print(f"User Terms: {', '.join(user_terms)}")
        print()
        
        best_approach = None
        best_score = 0
        
        for result in all_results:
            if not result['results']:
                continue
                
            top_result = result['results'][0]
            approach_name = result['approach']
            
            # Calculate alignment score based on approach type
            if approach_name == 'Term-Boosted Vector Search':
                alignment_score = top_result['combined_score']
                term_info = f"{len(top_result['exact_matches'])}/{len(user_terms)} exact matches"
                
            elif approach_name == 'User-Terminology Templates':
                alignment_score = top_result['semantic_score'] + (0.5 if top_result['contains_user_terms'] else 0)
                term_info = f"Uses user term: '{top_result['used_user_term']}'"
                
            elif approach_name == 'Exact-Term Prioritization':
                alignment_score = top_result['priority_score']
                term_info = f"{len(top_result['exact_matches'])}/{len(user_terms)} terms, {top_result['term_coverage']:.0%} coverage"
            
            print(f"📊 {approach_name}:")
            print(f"   Alignment Score: {alignment_score:.3f}")
            print(f"   Term Matching: {term_info}")
            print(f"   Top Result: {top_result.get('metadata', {}).get('title', 'Unknown')}")
            
            if alignment_score > best_score:
                best_score = alignment_score
                best_approach = approach_name
            print()
        
        if best_approach:
            print(f"🥇 WINNER: {best_approach} (Score: {best_score:.3f})")
            print("   This approach best preserved user's terminology while finding relevant content.")
        
        print(f"\n💡 Key Insight: Test with your specific use cases to see which approach")
        print(f"   maintains the best balance of relevance + user term alignment.")

def main():
    print("🎯 User Term Priority Testing Tool")
    print("=" * 80)
    print("Problem: Users search 'PAT setup' but get results about 'Personal Access Token'")
    print("Goal: Test approaches that prioritize user's exact terminology")
    print()
    print("📋 Testing 3 Approaches:")
    print("  1. Term-Boosted Search     - Combine semantic + exact term matching")
    print("  2. User-Terminology Templates - Echo user's words in responses")  
    print("  3. Exact-Term Prioritization - Heavily weight exact term matches")
    print("=" * 80)
    
    try:
        tester = UserTermPriorityTester()
        stats = tester.vm.get_collection_stats()
        print(f"✅ Connected to vector database ({stats['total_documents']} documents)")
    except Exception as e:
        print(f"❌ Failed to connect to vector database: {e}")
        print("Run: python vector-database/preparedocsforvectordb.py")
        return
    
    print("\n🔍 Commands:")
    print("  compare [query]  - Test all 3 approaches")
    print("  1 [query]       - Test Term-Boosted Search only")
    print("  2 [query]       - Test User-Terminology Templates only") 
    print("  3 [query]       - Test Exact-Term Prioritization only")
    print("  help            - Show help")
    print("  quit            - Exit")
    print()
    print("💡 Try these test queries:")
    print("  'PAT setup' | 'iOS build' | 'CI configuration' | 'environment variables'")
    print("-" * 80)
    
    while True:
        try:
            user_input = input("\n🎯 Test: ").strip()
            
            if not user_input or user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if user_input.lower() == 'help':
                print("\n📚 Commands:")
                print("  compare [query] - Compare all 3 approaches side-by-side")
                print("  1 [query]      - Term-Boosted Search (semantic + term matching)")
                print("  2 [query]      - User-Terminology Templates (echo user words)")
                print("  3 [query]      - Exact-Term Prioritization (heavy term weighting)")
                print("\n🎯 Focus: Each approach tries to solve the user terminology mismatch problem")
                continue
            
            # Parse command
            parts = user_input.split(' ', 1)
            if len(parts) < 2:
                print("❌ Please provide a query. Example: compare PAT setup")
                continue
                
            command, query = parts[0].lower(), parts[1]
            
            if command == 'compare':
                tester.compare_all_approaches(query)
            elif command == '1':
                result = tester.approach_1_term_boosted_search(query)
                tester._display_approach_results(result)
            elif command == '2':
                result = tester.approach_2_user_terminology_templates(query)
                tester._display_approach_results(result)
            elif command == '3':
                result = tester.approach_3_exact_term_prioritization(query)
                tester._display_approach_results(result)
            else:
                print("❌ Unknown command. Use 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()