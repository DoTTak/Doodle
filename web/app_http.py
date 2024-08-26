import http.server, ssl

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.headers)
        super().do_GET()

httpd = http.server.HTTPServer(('0.0.0.0', 80), CustomHandler)

httpd.serve_forever()