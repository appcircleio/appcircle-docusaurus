#!/usr/bin/env python3
"""
Complex Developer Query Testing
Test realistic "How to..." and "I want to..." queries that developers would actually ask
when working with Appcircle mobile CI/CD platform.
"""

import sys
import os
from datetime import datetime

# Add vector-database directory to Python path
vector_db_path = os.path.join(os.path.dirname(__file__), 'vector-database')
sys.path.insert(0, vector_db_path)

from test_user_term_priority import UserTermPriorityTester

class ComplexDeveloperQueryTester:
    def __init__(self):
        self.tester = UserTermPriorityTester()
        
        # Complex developer queries organized by scenario
        self.developer_queries = {
            "Getting Started Scenarios": [
                "How to setup automated CI/CD pipeline for my React Native app",
                "I want to migrate from GitHub Actions to Appcircle",
                "How to configure build environment for Flutter project with custom dependencies",
                "I want to setup parallel builds for iOS and Android from same repository"
            ],
            
            "Build & Configuration": [
                "How to setup environment variables for different deployment stages",
                "I want to use custom Docker images for my build environment",
                "How to configure build triggers when someone pushes to specific branches",
                "I want to cache node_modules to speed up React Native builds",
                "How to setup custom build scripts that run before compilation",
                "I want to build different app variants (debug, staging, production) automatically"
            ],
            
            "Testing Integration": [
                "How to integrate automated testing with Espresso for Android UI tests",
                "I want to run unit tests and UI tests in parallel during builds", 
                "How to setup code coverage reporting with Istanbul for React Native",
                "I want to automatically run tests before deploying to app stores",
                "How to configure Firebase Test Lab integration for automated device testing",
                "I want to fail builds if test coverage drops below 80%"
            ],
            
            "Code Signing & Security": [
                "How to setup iOS code signing with multiple developer certificates",
                "I want to automate certificate management without manual intervention",
                "How to configure Android signing for Google Play Store distribution",
                "I want to securely store API keys and certificates in build environment",
                "How to setup different signing configurations for debug and release builds",
                "I want to rotate certificates automatically before they expire"
            ],
            
            "Deployment & Distribution": [
                "How to automatically deploy to TestFlight after successful builds",
                "I want to deploy to multiple app stores (Apple, Google, Huawei) simultaneously", 
                "How to setup internal app distribution for beta testing team",
                "I want to automatically increment version numbers based on Git commits",
                "How to configure webhook notifications when deployment completes",
                "I want to setup staged rollout with automatic rollback on errors"
            ],
            
            "Advanced Workflows": [
                "How to setup custom workflow with dependency injection for microservices architecture",
                "I want to trigger builds across multiple repositories when core library changes",
                "How to configure matrix builds for different OS versions and device configurations",
                "I want to implement GitOps workflow with automatic environment promotion",
                "How to setup canary deployments with A/B testing integration",
                "I want to orchestrate complex multi-stage pipelines with manual approval gates"
            ],
            
            "Team & Enterprise": [
                "How to setup team access control with different permission levels",
                "I want to integrate with company LDAP for single sign-on authentication",
                "How to configure audit logging for compliance requirements",
                "I want to setup quota management for different teams and projects",
                "How to implement approval workflows for production deployments",
                "I want to setup cost allocation tracking per team and project"
            ],
            
            "Troubleshooting & Monitoring": [
                "How to debug build failures with detailed logging and artifacts",
                "I want to setup monitoring alerts when build success rate drops",
                "How to configure automatic retry logic for flaky network-dependent tests",
                "I want to analyze build performance metrics and optimize pipeline speed",
                "How to setup centralized logging with integration to Elasticsearch",
                "I want to create custom dashboards for build and deployment metrics"
            ]
        }
    
    def test_complex_query(self, query: str, show_details: bool = True) -> dict:
        """Test a single complex query and return detailed results"""
        print(f"\n🔍 Testing Query: '{query}'")
        print("-" * 80)
        
        # Use the best approach from our benchmark (Exact-Term Prioritization)
        result = self.tester.approach_3_exact_term_prioritization(query, n_results=3)
        
        if show_details and result['results']:
            for i, res in enumerate(result['results'][:2]):  # Show top 2 results
                metadata = res.get('metadata', {})
                title = metadata.get('title', 'Unknown Document')
                section = metadata.get('section', '')
                url = metadata.get('url', '')
                
                print(f"\n#{i+1} 📄 {title}")
                if section:
                    print(f"   📁 Section: {section}")
                if url:
                    print(f"   🔗 URL: {url}")
                
                print(f"   🏆 Priority Score: {res['priority_score']:.3f}")
                print(f"   🎯 Term Coverage: {res['term_coverage']:.1%} ({len(res['exact_matches'])}/{len(result['user_terms'])} terms)")
                print(f"   💡 {res['priority_explanation']}")
                print(f"   ✅ Found Terms: {', '.join(res['exact_matches']) if res['exact_matches'] else 'None'}")
                print(f"   ❌ Missing Terms: {', '.join(res['missing_terms']) if res['missing_terms'] else 'None'}")
                print(f"   📖 Preview: {res['content'][:200]}...")
                print("   " + "-" * 70)
        
        return {
            'query': query,
            'user_terms': result['user_terms'],
            'success': len(result['results']) > 0,
            'top_score': result['results'][0]['priority_score'] if result['results'] else 0,
            'term_coverage': result['results'][0]['term_coverage'] if result['results'] else 0,
            'exact_matches': result['results'][0]['exact_matches'] if result['results'] else [],
            'top_result_title': result['results'][0].get('metadata', {}).get('title', 'None') if result['results'] else 'None'
        }
    
    def run_developer_scenario_tests(self):
        """Run comprehensive testing of complex developer queries"""
        print("🎯 Complex Developer Query Testing")
        print("=" * 90)
        print("Testing realistic queries that developers would ask when using Appcircle CI/CD")
        print("=" * 90)
        
        all_results = []
        scenario_summaries = []
        
        for scenario, queries in self.developer_queries.items():
            print(f"\n📋 SCENARIO: {scenario}")
            print("=" * 60)
            
            scenario_results = []
            successful_queries = 0
            high_quality_results = 0
            excellent_term_coverage = 0
            
            for query in queries:
                result = self.test_complex_query(query, show_details=True)
                scenario_results.append(result)
                all_results.append(result)
                
                if result['success']:
                    successful_queries += 1
                    
                    # High quality = good priority score + term coverage
                    if result['top_score'] > 0.8 and result['term_coverage'] > 0.5:
                        high_quality_results += 1
                    
                    # Excellent term coverage
                    if result['term_coverage'] >= 0.7:
                        excellent_term_coverage += 1
            
            # Scenario summary
            total_queries = len(queries)
            success_rate = (successful_queries / total_queries) * 100
            quality_rate = (high_quality_results / total_queries) * 100
            term_coverage_rate = (excellent_term_coverage / total_queries) * 100
            
            scenario_summary = {
                'scenario': scenario,
                'total_queries': total_queries,
                'successful_queries': successful_queries,
                'success_rate': success_rate,
                'high_quality_results': high_quality_results,
                'quality_rate': quality_rate,
                'excellent_term_coverage': excellent_term_coverage,
                'term_coverage_rate': term_coverage_rate
            }
            scenario_summaries.append(scenario_summary)
            
            print(f"\n📊 {scenario} Summary:")
            print(f"   ✅ Successful Results: {successful_queries}/{total_queries} ({success_rate:.1f}%)")
            print(f"   🏆 High Quality Results: {high_quality_results}/{total_queries} ({quality_rate:.1f}%)")
            print(f"   🎯 Excellent Term Coverage: {excellent_term_coverage}/{total_queries} ({term_coverage_rate:.1f}%)")
        
        # Overall analysis
        self.display_overall_analysis(all_results, scenario_summaries)
        
        # Save detailed results
        self.save_complex_query_results(all_results, scenario_summaries)
        
        return all_results, scenario_summaries
    
    def display_overall_analysis(self, all_results, scenario_summaries):
        """Display comprehensive analysis of all complex queries"""
        print(f"\n{'='*90}")
        print("🏆 OVERALL COMPLEX QUERY ANALYSIS")
        print(f"{'='*90}")
        
        total_queries = len(all_results)
        successful = sum(1 for r in all_results if r['success'])
        high_scores = sum(1 for r in all_results if r['top_score'] > 0.8)
        good_coverage = sum(1 for r in all_results if r['term_coverage'] > 0.5)
        
        print(f"📊 Overall Performance ({total_queries} complex queries):")
        print(f"   ✅ Successful Results: {successful}/{total_queries} ({(successful/total_queries)*100:.1f}%)")
        print(f"   🏆 High Priority Scores (>0.8): {high_scores}/{total_queries} ({(high_scores/total_queries)*100:.1f}%)")
        print(f"   🎯 Good Term Coverage (>50%): {good_coverage}/{total_queries} ({(good_coverage/total_queries)*100:.1f}%)")
        
        print(f"\n📋 Performance by Scenario:")
        for summary in scenario_summaries:
            scenario_name = summary['scenario'][:25] + "..." if len(summary['scenario']) > 25 else summary['scenario']
            print(f"   {scenario_name:<30} Success: {summary['success_rate']:5.1f}%  Quality: {summary['quality_rate']:5.1f}%")
        
        # Top performing and challenging queries
        top_results = sorted([r for r in all_results if r['success']], key=lambda x: x['top_score'], reverse=True)[:3]
        challenging_results = sorted([r for r in all_results if r['success']], key=lambda x: x['top_score'])[:3]
        
        print(f"\n🥇 TOP PERFORMING QUERIES:")
        for i, result in enumerate(top_results, 1):
            print(f"   {i}. Score {result['top_score']:.3f} | Coverage {result['term_coverage']:.1%} | \"{result['query'][:60]}...\"")
        
        print(f"\n🔧 MOST CHALLENGING QUERIES:")
        for i, result in enumerate(challenging_results, 1):
            print(f"   {i}. Score {result['top_score']:.3f} | Coverage {result['term_coverage']:.1%} | \"{result['query'][:60]}...\"")
        
        # Insights and recommendations
        print(f"\n💡 KEY INSIGHTS:")
        avg_score = sum(r['top_score'] for r in all_results if r['success']) / successful if successful > 0 else 0
        avg_coverage = sum(r['term_coverage'] for r in all_results if r['success']) / successful if successful > 0 else 0
        
        print(f"   📈 Average Priority Score: {avg_score:.3f}")
        print(f"   📈 Average Term Coverage: {avg_coverage:.1%}")
        
        if avg_score > 0.7:
            print(f"   ✅ EXCELLENT: Term Priority Search handles complex developer queries very well")
        elif avg_score > 0.5:
            print(f"   👍 GOOD: Term Priority Search performs well on most complex queries")
        else:
            print(f"   ⚠️  NEEDS IMPROVEMENT: Consider enhancing search algorithm for complex queries")
            
        if avg_coverage > 0.6:
            print(f"   ✅ STRONG: Excellent user terminology alignment in complex scenarios")
        elif avg_coverage > 0.4:
            print(f"   👍 ADEQUATE: Good terminology matching for most developer queries")
        else:
            print(f"   ⚠️  WEAK: May need better term extraction for complex developer language")
    
    def save_complex_query_results(self, all_results, scenario_summaries):
        """Save detailed results to JSON file"""
        import json
        
        output_data = {
            'timestamp': datetime.now().isoformat(),
            'test_type': 'complex_developer_queries',
            'total_queries': len(all_results),
            'scenario_summaries': scenario_summaries,
            'detailed_results': all_results,
            'performance_metrics': {
                'avg_priority_score': sum(r['top_score'] for r in all_results if r['success']) / sum(1 for r in all_results if r['success']) if any(r['success'] for r in all_results) else 0,
                'avg_term_coverage': sum(r['term_coverage'] for r in all_results if r['success']) / sum(1 for r in all_results if r['success']) if any(r['success'] for r in all_results) else 0,
                'overall_success_rate': (sum(1 for r in all_results if r['success']) / len(all_results)) * 100
            }
        }
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"complex_developer_queries_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(output_data, f, indent=2, default=str)
        
        print(f"\n💾 Detailed results saved to: {filename}")

def main():
    print("🎯 Complex Developer Query Testing Tool")
    print("Testing realistic 'How to...' and 'I want to...' queries")
    print("that developers would ask when working with Appcircle CI/CD")
    print("=" * 80)
    
    try:
        tester = ComplexDeveloperQueryTester()
        print("✅ Connected to vector database")
        
        # Run comprehensive testing
        all_results, scenario_summaries = tester.run_developer_scenario_tests()
        
        print(f"\n🎉 Complex query testing completed!")
        print(f"Tested {len(all_results)} realistic developer scenarios")
        
    except Exception as e:
        print(f"❌ Testing failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()