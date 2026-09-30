from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Event, Thread

class HelloWorldHandler_01(BaseHTTPRequestHandler):
    # Responde às requisições GET com a primeira página de exemplo.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        response = b"<html><body><h1>Hello World 1</h1></body></html>"
        self.wfile.write(response)

    # Desativa os logs padrão de acesso do servidor.
    def log_message(self, format, *args):
        pass

class HelloWorldHandler_02(BaseHTTPRequestHandler):
    # Responde às requisições GET com a segunda página de exemplo.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        response = b"<html><body><h1>Hello World 2</h1></body></html>"
        self.wfile.write(response)

    # Desativa os logs padrão de acesso do servidor.
    def log_message(self, format, *args):
        pass    

if __name__ == "__main__":
    # Cada servidor usa uma porta e um handler próprios.
    server_01 = HTTPServer(("0.0.0.0", 8001), HelloWorldHandler_01)
    server_02 = HTTPServer(("0.0.0.0", 8002), HelloWorldHandler_02)

    # Executa cada servidor em sua própria thread dedicada.
    Thread(target=server_01.serve_forever, daemon=True).start()
    Thread(target=server_02.serve_forever, daemon=True).start()
    print("Servidor 1 em http://localhost:8001")
    print("Servidor 2 em http://localhost:8002")

    try:
        Event().wait()
    except KeyboardInterrupt:
        server_01.shutdown()
        server_02.shutdown()