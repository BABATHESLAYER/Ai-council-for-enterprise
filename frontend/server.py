#!/usr/bin/env python3
"""
Simple HTTP server to serve the frontend and handle CORS for API requests.
Run: python frontend/server.py
Then open: http://localhost:3000
"""
import http.server
import socketserver
import os
from pathlib import Path

PORT = 3000
FRONTEND_DIR = Path(__file__).parent.absolute()

class FrontendHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(FRONTEND_DIR), **kwargs)

    def end_headers(self):
        """Add CORS headers to allow API calls to localhost:8000"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        """Custom logging"""
        print(f"[Frontend] {format % args}")


if __name__ == '__main__':
    os.chdir(FRONTEND_DIR)
    with socketserver.TCPServer(("", PORT), FrontendHandler) as httpd:
        print(f"""
╔════════════════════════════════════════════════════════════════╗
║         AI Enterprise Council - Frontend Server              ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  Frontend:  http://localhost:{PORT}                              ║
║  API:       http://localhost:8000                              ║
║             (make sure docker compose is running)              ║
║                                                                ║
║  Serving files from: {FRONTEND_DIR}        ║
║                                                                ║
║  Press Ctrl+C to stop                                          ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
        """)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[Frontend] Server stopped.")
