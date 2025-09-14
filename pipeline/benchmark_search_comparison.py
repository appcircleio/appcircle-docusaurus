#!/usr/bin/env python3
"""
Benchmark Search Comparison Tool
Comprehensive testing of test_vector_search.py vs test_user_term_priority.py

Tests both approaches with queries from simple to advanced Appcircle CI/CD scenarios
to determine which provides better user experience and relevance.
"""

import json
import time
from datetime import datetime
from typing import Dict, List, Any
import sys
import os

# Add vector-database directory to Python path
vector_db_path = os.path.join(os.path.dirname(__file__), 'vector-database')
sys.path.insert(0, vector_db_path)

from preparedocsforvectordb import VectorDatabaseManager
from test_user_term_priority import UserTermPriorityTester

class SearchBenchmark:
    def __init__(self):
        self.vm = VectorDatabaseManager('vector_db', 'all-MiniLM-L6-v2')
        self.vm.initialize()
        self.term_tester = UserTermPriorityTester()
        
        # Comprehensive test queries from simple to advanced
        self.test_queries = {
            "Simple Queries": [
                "PAT",
                "iOS build",
                "API key",
                "environment variables",
                "code signing",
                "test",
                "deploy"
            ],
            
            "Common User Questions": [
                "how to setup PAT",
                "create iOS build",
                "configure environment variables",
                "setup code signing",
                "run tests",
                "deploy to app store",
                "connect to GitHub"
            ],
            
            "Specific Features": [
                "PAT setup",
                "build profile creation",
                "environment variable configuration",
                "iOS code signing certificates", 
                "Android signing for Google Play",
                "automated testing setup",
                "app store deployment",
                "webhook notifications"
            ],
            
            "Advanced Scenarios": [
                "how to build Flutter app with custom environment variables",
                "configure iOS code signing with multiple certificates",
                "setup CI/CD pipeline for React Native with automated testing",
                "deploy to multiple app stores with different configurations",
                "integrate custom scripts in build workflow",
                "setup enterprise distribution with LDAP authentication",
                "configure self-hosted runner with specific requirements"
            ],
            
            "Abbreviation Heavy": [
                "CI configuration",
                "CD pipeline setup", 
                "API integration",
                "SDK configuration",
                "CLI commands",
                "LDAP authentication",
                "SSO setup",
                "PAT for API access"
            ],
            
            "Edge Cases": [
                "troubleshooting build failures",
                "certificate expired",
                "build timeout issues",
                "missing dependencies",
                "authentication errors",
                "webhook not working",
                "runner offline"
            ]
        }
    
    def test_basic_vector_search(self, query: str) -> Dict[str, Any]:
        """Test the basic vector search approach"""
        start_time = time.time()
        
        try:
            results = self.vm.search_similar(query, n_results=3)
            end_time = time.time()
            
            if not results['documents'][0]:
                return {
                    'success': False,
                    'error': 'No results found',
                    'response_time': end_time - start_time
                }
            
            # Process results similar to test_vector_search.py
            processed_results = []
            for i, (doc, metadata, distance) in enumerate(zip(
                results['documents'][0][:3],
                results['metadatas'][0][:3], 
                results['distances'][0][:3]
            )):
                similarity = 1 - distance
                processed_results.append({
                    'title': metadata.get('title', 'Unknown'),
                    'section': metadata.get('section', 'N/A'),
                    'url': metadata.get('url', ''),
                    'description': metadata.get('description', ''),
                    'similarity_score': similarity,
                    'content_preview': doc[:200],
                    'relevance_tier': self._get_relevance_tier(similarity)
                })
            
            return {
                'success': True,
                'approach': 'Basic Vector Search',
                'results': processed_results,
                'response_time': end_time - start_time,
                'top_similarity': processed_results[0]['similarity_score'] if processed_results else 0
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'response_time': time.time() - start_time
            }
    
    def test_term_priority_search(self, query: str) -> Dict[str, Any]:
        """Test the term priority approach (best performing method from the 3 approaches)"""
        start_time = time.time()
        
        try:
            # Use approach 3 (Exact-Term Prioritization) as it typically performs best
            result = self.term_tester.approach_3_exact_term_prioritization(query, n_results=3)
            end_time = time.time()
            
            if not result['results']:
                return {
                    'success': False,
                    'error': 'No results found',
                    'response_time': end_time - start_time
                }
            
            # Process results for comparison
            processed_results = []
            for res in result['results']:
                metadata = res.get('metadata', {})
                processed_results.append({
                    'title': metadata.get('title', 'Unknown'),
                    'section': metadata.get('section', 'N/A'),
                    'url': metadata.get('url', ''),
                    'description': metadata.get('description', ''),
                    'priority_score': res['priority_score'],
                    'term_coverage': res['term_coverage'],
                    'exact_matches': res['exact_matches'],
                    'content_preview': res['content'][:200],
                    'priority_explanation': res['priority_explanation']
                })
            
            return {
                'success': True,
                'approach': 'Term Priority Search',
                'results': processed_results,
                'response_time': end_time - start_time,
                'user_terms': result['user_terms'],
                'top_priority_score': processed_results[0]['priority_score'] if processed_results else 0,
                'term_alignment_quality': self._calculate_term_alignment_quality(result)
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'response_time': time.time() - start_time
            }
    
    def _get_relevance_tier(self, similarity: float) -> str:
        """Categorize relevance based on similarity score"""
        if similarity > 0.7:
            return "High"
        elif similarity > 0.4:
            return "Good" 
        elif similarity > 0.2:
            return "Moderate"
        else:
            return "Low"
    
    def _calculate_term_alignment_quality(self, result: Dict) -> float:
        """Calculate how well the approach aligns with user terminology"""
        if not result['results']:
            return 0.0
        
        top_result = result['results'][0]
        user_terms = result['user_terms']
        
        if not user_terms:
            return 0.5  # Neutral score if no user terms extracted
        
        # Weight term coverage heavily for alignment quality
        term_coverage_weight = 0.7
        priority_score_weight = 0.3
        
        term_coverage = top_result['term_coverage']
        normalized_priority = min(top_result['priority_score'] / 1.5, 1.0)  # Normalize to 0-1
        
        alignment_quality = (term_coverage * term_coverage_weight) + (normalized_priority * priority_score_weight)
        return alignment_quality
    
    def run_comprehensive_benchmark(self) -> Dict[str, Any]:
        """Run comprehensive benchmark comparing both approaches"""
        print("🚀 Starting Comprehensive Search Benchmark")
        print("=" * 80)
        
        benchmark_results = {
            'timestamp': datetime.now().isoformat(),
            'total_queries': 0,
            'categories': {},
            'summary_comparison': {},
            'detailed_results': []
        }
        
        total_queries = sum(len(queries) for queries in self.test_queries.values())
        benchmark_results['total_queries'] = total_queries
        current_query = 0
        
        for category, queries in self.test_queries.items():
            print(f"\n📋 Testing Category: {category}")
            print("-" * 60)
            
            category_results = {
                'basic_vector_wins': 0,
                'term_priority_wins': 0,
                'ties': 0,
                'basic_vector_avg_time': 0,
                'term_priority_avg_time': 0,
                'queries_tested': len(queries),
                'detailed_comparisons': []
            }
            
            basic_times = []
            term_times = []
            
            for query in queries:
                current_query += 1
                print(f"🔍 [{current_query}/{total_queries}] Testing: '{query}'")
                
                # Test both approaches
                basic_result = self.test_basic_vector_search(query)
                term_result = self.test_term_priority_search(query)
                
                basic_times.append(basic_result.get('response_time', 0))
                term_times.append(term_result.get('response_time', 0))
                
                # Determine winner based on multiple criteria
                winner = self._determine_winner(basic_result, term_result, query)
                
                if winner == 'basic':
                    category_results['basic_vector_wins'] += 1
                elif winner == 'term_priority':
                    category_results['term_priority_wins'] += 1
                else:
                    category_results['ties'] += 1
                
                # Store detailed comparison
                comparison = {
                    'query': query,
                    'winner': winner,
                    'basic_vector_result': basic_result,
                    'term_priority_result': term_result,
                    'winner_reasoning': self._explain_winner_choice(basic_result, term_result, winner)
                }
                
                category_results['detailed_comparisons'].append(comparison)
                benchmark_results['detailed_results'].append(comparison)
                
                # Show quick summary
                if basic_result['success'] and term_result['success']:
                    basic_title = basic_result['results'][0]['title'] if basic_result['results'] else 'N/A'
                    term_title = term_result['results'][0]['title'] if term_result['results'] else 'N/A'
                    print(f"   🥇 Winner: {winner.replace('_', ' ').title()}")
                    print(f"   📄 Basic: {basic_title}")
                    print(f"   🎯 Term:  {term_title}")
            
            # Calculate averages
            category_results['basic_vector_avg_time'] = sum(basic_times) / len(basic_times) if basic_times else 0
            category_results['term_priority_avg_time'] = sum(term_times) / len(term_times) if term_times else 0
            
            benchmark_results['categories'][category] = category_results
            
            # Show category summary
            print(f"\n📊 {category} Summary:")
            print(f"   Basic Vector Search wins: {category_results['basic_vector_wins']}")
            print(f"   Term Priority Search wins: {category_results['term_priority_wins']}")
            print(f"   Ties: {category_results['ties']}")
            print(f"   Avg Response Time - Basic: {category_results['basic_vector_avg_time']:.3f}s")
            print(f"   Avg Response Time - Term: {category_results['term_priority_avg_time']:.3f}s")
        
        # Calculate overall summary
        benchmark_results['summary_comparison'] = self._calculate_overall_summary(benchmark_results)
        
        return benchmark_results
    
    def _determine_winner(self, basic_result: Dict, term_result: Dict, query: str) -> str:
        """Determine winner based on multiple criteria"""
        if not basic_result['success'] and not term_result['success']:
            return 'tie'
        elif not basic_result['success']:
            return 'term_priority'
        elif not term_result['success']:
            return 'basic'
        
        # Scoring criteria (weights can be adjusted)
        criteria_weights = {
            'relevance_score': 0.4,  # How relevant is the top result
            'term_alignment': 0.35,  # How well does it match user terms
            'response_time': 0.15,   # Speed matters
            'result_quality': 0.1    # Overall result quality
        }
        
        basic_score = 0
        term_score = 0
        
        # 1. Relevance Score
        basic_relevance = basic_result.get('top_similarity', 0)
        term_relevance = term_result.get('top_priority_score', 0) / 2  # Normalize priority score
        
        if basic_relevance > term_relevance:
            basic_score += criteria_weights['relevance_score']
        elif term_relevance > basic_relevance:
            term_score += criteria_weights['relevance_score']
        
        # 2. Term Alignment (crucial for user experience)
        user_terms = term_result.get('user_terms', [])
        term_alignment_quality = term_result.get('term_alignment_quality', 0)
        
        # Term priority approach inherently better at term alignment
        if user_terms and len(user_terms) > 0:
            term_score += criteria_weights['term_alignment']
            
            # Check if basic search result contains user terms
            basic_content = basic_result['results'][0]['content_preview'].lower() if basic_result['results'] else ''
            user_term_matches = sum(1 for term in user_terms if term.lower() in basic_content)
            basic_term_alignment = user_term_matches / len(user_terms) if user_terms else 0
            
            if basic_term_alignment < 0.5:  # If basic search doesn't align well with terms
                term_score += criteria_weights['term_alignment'] * 0.5  # Bonus to term priority
        
        # 3. Response Time (faster is better)
        basic_time = basic_result.get('response_time', 1.0)
        term_time = term_result.get('response_time', 1.0)
        
        if basic_time < term_time:
            basic_score += criteria_weights['response_time']
        elif term_time < basic_time:
            term_score += criteria_weights['response_time']
        
        # 4. Result Quality (title relevance, description quality)
        basic_quality = self._assess_result_quality(basic_result, query)
        term_quality = self._assess_result_quality(term_result, query)
        
        if basic_quality > term_quality:
            basic_score += criteria_weights['result_quality']
        elif term_quality > basic_quality:
            term_score += criteria_weights['result_quality']
        
        # Determine winner
        if abs(basic_score - term_score) < 0.1:  # Very close scores
            return 'tie'
        elif basic_score > term_score:
            return 'basic'
        else:
            return 'term_priority'
    
    def _assess_result_quality(self, result: Dict, query: str) -> float:
        """Assess overall quality of search results"""
        if not result['success'] or not result['results']:
            return 0.0
        
        top_result = result['results'][0]
        quality_score = 0.0
        
        # Title relevance
        title = top_result.get('title', '').lower()
        query_lower = query.lower()
        if any(word in title for word in query_lower.split()):
            quality_score += 0.3
        
        # Has description
        if top_result.get('description'):
            quality_score += 0.2
        
        # Has URL for navigation
        if top_result.get('url'):
            quality_score += 0.2
        
        # Content preview quality (not empty, reasonable length)
        content = top_result.get('content_preview', '')
        if len(content) > 50:
            quality_score += 0.3
        
        return quality_score
    
    def _explain_winner_choice(self, basic_result: Dict, term_result: Dict, winner: str) -> str:
        """Explain why a particular approach won"""
        if winner == 'tie':
            return "Both approaches performed similarly"
        elif winner == 'basic':
            reasons = []
            if basic_result.get('top_similarity', 0) > 0.7:
                reasons.append("high semantic similarity")
            if basic_result.get('response_time', 1) < term_result.get('response_time', 1):
                reasons.append("faster response")
            return f"Basic vector search won due to: {', '.join(reasons)}"
        else:  # term_priority
            reasons = []
            if term_result.get('term_alignment_quality', 0) > 0.7:
                reasons.append("excellent term alignment")
            user_terms = term_result.get('user_terms', [])
            if user_terms and len(user_terms) > 1:
                reasons.append(f"matched {len(user_terms)} user terms")
            return f"Term priority search won due to: {', '.join(reasons)}"
    
    def _calculate_overall_summary(self, benchmark_results: Dict) -> Dict:
        """Calculate overall performance summary"""
        total_basic_wins = 0
        total_term_wins = 0
        total_ties = 0
        total_basic_time = 0
        total_term_time = 0
        total_queries = 0
        
        for category_results in benchmark_results['categories'].values():
            total_basic_wins += category_results['basic_vector_wins']
            total_term_wins += category_results['term_priority_wins']
            total_ties += category_results['ties']
            total_basic_time += category_results['basic_vector_avg_time'] * category_results['queries_tested']
            total_term_time += category_results['term_priority_avg_time'] * category_results['queries_tested']
            total_queries += category_results['queries_tested']
        
        return {
            'overall_winner': 'basic' if total_basic_wins > total_term_wins else 'term_priority' if total_term_wins > total_basic_wins else 'tie',
            'basic_vector_wins': total_basic_wins,
            'term_priority_wins': total_term_wins, 
            'ties': total_ties,
            'basic_win_percentage': (total_basic_wins / total_queries) * 100,
            'term_priority_win_percentage': (total_term_wins / total_queries) * 100,
            'overall_basic_avg_time': total_basic_time / total_queries,
            'overall_term_avg_time': total_term_time / total_queries,
            'total_queries_tested': total_queries
        }
    
    def save_benchmark_results(self, results: Dict, filename: str = 'benchmark_results.json'):
        """Save detailed benchmark results to file"""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"💾 Detailed benchmark results saved to: {filename}")
    
    def display_final_analysis(self, results: Dict):
        """Display comprehensive final analysis"""
        summary = results['summary_comparison']
        
        print(f"\n{'='*80}")
        print("🏆 FINAL BENCHMARK ANALYSIS")
        print(f"{'='*80}")
        
        print(f"📊 Overall Results ({summary['total_queries_tested']} queries tested):")
        print(f"   🔵 Basic Vector Search: {summary['basic_vector_wins']} wins ({summary['basic_win_percentage']:.1f}%)")
        print(f"   🟡 Term Priority Search: {summary['term_priority_wins']} wins ({summary['term_priority_win_percentage']:.1f}%)")
        print(f"   ⚪ Ties: {summary['ties']} ({(summary['ties']/summary['total_queries_tested'])*100:.1f}%)")
        
        print(f"\n⚡ Performance:")
        print(f"   Basic Vector Search avg time: {summary['overall_basic_avg_time']:.3f}s")
        print(f"   Term Priority Search avg time: {summary['overall_term_avg_time']:.3f}s")
        
        winner = summary['overall_winner']
        if winner != 'tie':
            winner_name = "Basic Vector Search" if winner == 'basic' else "Term Priority Search"
            print(f"\n🥇 OVERALL WINNER: {winner_name}")
        else:
            print(f"\n🤝 RESULT: Tie - Both approaches have their strengths")
        
        # Category breakdown
        print(f"\n📋 Performance by Category:")
        for category, results in results['categories'].items():
            basic_wins = results['basic_vector_wins']
            term_wins = results['term_priority_wins']
            ties = results['ties']
            total = results['queries_tested']
            
            if basic_wins > term_wins:
                category_winner = "Basic Vector"
            elif term_wins > basic_wins:
                category_winner = "Term Priority" 
            else:
                category_winner = "Tie"
                
            print(f"   {category}: {category_winner} ({basic_wins}B-{term_wins}T-{ties}Tie/{total})")
        
        # Recommendations
        print(f"\n💡 RECOMMENDATIONS:")
        if winner == 'basic':
            print("   ✅ Use Basic Vector Search for:")
            print("      - High-performance requirements (faster response)")
            print("      - Semantic similarity is most important")
            print("      - General documentation search")
        elif winner == 'term_priority':
            print("   ✅ Use Term Priority Search for:")
            print("      - User terminology alignment is crucial")
            print("      - Queries with specific abbreviations (PAT, CI, etc.)")
            print("      - When users expect their exact words in results")
        else:
            print("   ✅ Hybrid Approach Recommended:")
            print("      - Use Term Priority for abbreviation-heavy queries")
            print("      - Use Basic Vector for general semantic search")
            print("      - Consider user context and query type")

def main():
    print("🔬 Search Approach Benchmark Tool")
    print("Comprehensive comparison of Basic Vector Search vs Term Priority Search")
    print("=" * 80)
    
    try:
        benchmark = SearchBenchmark()
        print("✅ Connected to vector database")
        
        # Run comprehensive benchmark
        results = benchmark.run_comprehensive_benchmark()
        
        # Display final analysis
        benchmark.display_final_analysis(results)
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"benchmark_results_{timestamp}.json"
        benchmark.save_benchmark_results(results, filename)
        
        print(f"\n🎯 Benchmark completed! Check {filename} for detailed results.")
        
    except Exception as e:
        print(f"❌ Benchmark failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()