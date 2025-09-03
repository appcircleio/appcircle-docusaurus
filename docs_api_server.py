#!/usr/bin/env python3
"""
Simple HTTP API server for documentation search
Can be used with MCP or direct API calls for chatbot integration
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import sys
from docs_search_api import DocsSearchAPI


# Global search API instance
search_api = DocsSearchAPI()

class DocsAPIHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)
        
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        
        try:
            if path == '/search':
                self._handle_search(query_params)
            elif path == '/sections':
                self._handle_sections()
            elif path == '/section':
                self._handle_section_docs(query_params)
            elif path == '/document':
                self._handle_get_document(query_params)
            elif path == '/health':
                self._handle_health()
            elif path == '/':
                self._handle_root()
            else:
                self._send_error(404, "Endpoint not found")
        except Exception as e:
            self._send_error(500, f"Internal server error: {str(e)}")
    
    def do_OPTIONS(self):
        """Handle OPTIONS requests for CORS"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def _handle_search(self, query_params):
        """Handle search endpoint"""
        query = query_params.get('q', [''])[0]
        max_results = int(query_params.get('limit', ['10'])[0])
        
        if not query:
            self._send_error(400, "Missing 'q' parameter")
            return
        
        results = search_api.search(query, max_results)
        response = {
            "query": query,
            "total_results": len(results),
            "results": results
        }
        
        self._send_json_response(response)
    
    def _handle_sections(self):
        """Handle sections endpoint"""
        sections = search_api.get_sections()
        response = {
            "sections": sections,
            "total_sections": len(sections)
        }
        
        self._send_json_response(response)
    
    def _handle_section_docs(self, query_params):
        """Handle section documents endpoint"""
        section = query_params.get('name', [''])[0]
        max_results = int(query_params.get('limit', ['20'])[0])
        
        if not section:
            self._send_error(400, "Missing 'name' parameter")
            return
        
        results = search_api.search_by_section(section, max_results)
        response = {
            "section": section,
            "total_results": len(results),
            "results": results
        }
        
        self._send_json_response(response)
    
    def _handle_get_document(self, query_params):
        """Handle get document endpoint"""
        doc_id = query_params.get('id', [''])[0]
        
        if not doc_id:
            self._send_error(400, "Missing 'id' parameter")
            return
        
        document = search_api.get_document_by_id(doc_id)
        if not document:
            self._send_error(404, "Document not found")
            return
        
        self._send_json_response(document)
    
    def _handle_health(self):
        """Handle health check endpoint"""
        response = {
            "status": "healthy",
            "indexed_documents": search_api.index.get("total_documents", 0),
            "api_version": "1.0"
        }
        self._send_json_response(response)
    
    def _handle_root(self):
        """Handle root endpoint with API documentation"""
        docs = {
            "message": "Appcircle Documentation Search API",
            "endpoints": {
                "/search?q=<query>&limit=<n>": "Search documentation",
                "/sections": "List all available sections",
                "/section?name=<section>&limit=<n>": "Get documents from a section",
                "/document?id=<doc_id>": "Get full document content",
                "/health": "API health check"
            },
            "examples": {
                "search": "/search?q=build profile&limit=5",
                "section": "/section?name=build&limit=10",
                "document": "/document?id=build-manage-the-connections-adding-a-build-profile"
            }
        }
        self._send_json_response(docs)
    
    def _send_json_response(self, data):
        """Send JSON response"""
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        json_data = json.dumps(data, indent=2, ensure_ascii=False)
        self.wfile.write(json_data.encode('utf-8'))
    
    def _send_error(self, code, message):
        """Send error response"""
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        error_data = {"error": message, "code": code}
        json_data = json.dumps(error_data, indent=2)
        self.wfile.write(json_data.encode('utf-8'))
    
    def log_message(self, format, *args):
        """Override to provide cleaner logging"""
        print(f"[{self.address_string()}] {format % args}")


def run_server(port=8000):
    """Run the documentation API server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, DocsAPIHandler)
    
    print(f"🚀 Appcircle Docs API Server starting on port {port}")
    print(f"🔗 Access the API at: http://localhost:{port}")
    print(f"📖 API documentation: http://localhost:{port}/")
    print(f"🔍 Example search: http://localhost:{port}/search?q=build%20profile")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
        httpd.server_close()


if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 8000.")
    
    run_server(port)