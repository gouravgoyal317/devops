from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

Handler = SimpleHTTPRequestHandler
httpd = HTTPServer(("0.0.0.0", PORT), Handler)

print("Server running on port 8000")

httpd.serve_forever()
