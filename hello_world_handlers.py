from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse


class HelloWorldRouterHandler(BaseHTTPRequestHandler):
    def send_html(self, content: str, status_code: int = 200):
        self.send_response(status_code)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

    def do_GET(self):
        parsed_path = urlparse(self.path).path

        if parsed_path in ("/", "/hello"):
            self.send_html(
                "<html><body><h1>Hello World</h1><p>Rotas: <a href='/1'>/1</a> | <a href='/2'>/2</a></p></body></html>"
            )
        elif parsed_path in ("/1", "/hello1"):
            self.send_html("<html><body><h1>Hello World 1 (v1.3.0) </h1></body></html>")
        elif parsed_path in ("/2", "/hello2"):
            self.send_html("<html><body><h1>Hello World 2 (v1.3.0)</h1></body></html>")
        else:
            self.send_html(
                "<html><body><h1>404 - Rota não encontrada</h1></body></html>",
                status_code=404,
            )

    def log_message(self, format, *args):
        pass
