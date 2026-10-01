from http.server import BaseHTTPRequestHandler


class HelloWorldHandler01(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        response = b"<html><body><h1>Hello World 1</h1></body></html>"
        self.wfile.write(response)

    def log_message(self, format, *args):
        pass


class HelloWorldHandler02(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        response = b"<html><body><h1>Hello World 2</h1></body></html>"
        self.wfile.write(response)

    def log_message(self, format, *args):
        pass
