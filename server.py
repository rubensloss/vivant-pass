import http.server
import socketserver
import sys

PORT = 3001

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    print(f"Starting VivantPass server on port {PORT} with strict no-cache headers...")
    sys.stdout.flush()
    with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
        httpd.serve_forever()
