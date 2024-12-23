import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create handler object
handler = MyHttpRequestHandler

# Create server object
port = 8000
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving at port {port}")
    # Start the server
    httpd.serve_forever() 