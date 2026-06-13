from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        html = """
        <html>
        <head>
            <title>Preview Environment Demo</title>
            <style>
            body {
                font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
                margin: 0;
                padding: 40px;
                background: #ffffff;
                color: #111827;
                text-align: center;
            }
            h1 {
                font-size: 32px;
                margin-bottom: 8px;
            }
            p {
                margin: 4px 0;
                color: #4b5563;
            }
            </style>
        </head>
        <body>
            <h1>Hello from your PR preview</h1>
            <p>This is a simple demo page served from a Docker container.</p>
            <p>Each pull request can have its own URL and isolated environment.</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    port = 80
    server = HTTPServer(("", port), Handler)
    print(f"Serving on port {port}…")
    server.serve_forever()