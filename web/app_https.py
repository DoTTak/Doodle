import os
import http.server, ssl

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.headers)
        super().do_GET()

httpd = http.server.HTTPServer(('0.0.0.0', 443), CustomHandler)

httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               keyfile='cert/server.key',
                               certfile='cert/server.crt',
                               ssl_version=ssl.PROTOCOL_TLS)

httpd.serve_forever()