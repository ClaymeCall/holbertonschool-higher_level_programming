#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 8000


class Server(BaseHTTPRequestHandler):
    '''
    This class includes basic components for a HTTP server
    '''

    def do_GET(self):
        '''
        Handles GET requests.
        '''
        match self.path:
            case "/":
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b'Hello, this is a simple API!')

            case "/data":
                data = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                }
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())

            case "/info":
                info = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(info).encode())

            case "/status":
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"OK")

            case _:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"Endpoint not found")

if __name__ is "__main__":
    with HTTPServer(("", PORT), Server) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
