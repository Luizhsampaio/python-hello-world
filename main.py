# Importa as classes necessárias para criar um servidor HTTP simples em Python.
from http.server import BaseHTTPRequestHandler, HTTPServer

# Define um manipulador de requisições HTTP.
# Ele herda de BaseHTTPRequestHandler e responde às requisições GET.
class HelloWorldHandler(BaseHTTPRequestHandler):
    # Este método é chamado quando o servidor recebe uma requisição GET.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        response = b"<html><body><h1>Hello World</h1></body></html>"
        self.wfile.write(response)

    # Sobrescreve o método que registra mensagens de log do servidor.
    def log_message(self, format, *args):
        pass


# Bloco principal: executa apenas quando o arquivo é rodado diretamente.
if __name__ == "__main__":
    # Cria um servidor HTTP ouvindo em todas as interfaces da máquina na porta 8001.
    server = HTTPServer(("0.0.0.0", 8001), HelloWorldHandler)
    # Exibe a URL onde o servidor está disponível.
    print("Servidor em http://localhost:8001")
    # Mantém o servidor em execução aguardando requisições.
    server.serve_forever()