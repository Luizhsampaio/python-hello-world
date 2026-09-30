# Importa as classes necessárias para criar um servidor HTTP simples em Python.
from http.server import BaseHTTPRequestHandler, HTTPServer

# Define um manipulador de requisições HTTP.
# Ele herda de BaseHTTPRequestHandler e responde às requisições GET.
class HelloWorldHandler(BaseHTTPRequestHandler):
    # Este método é chamado quando o servidor recebe uma requisição GET.
    def do_GET(self):
        # Envia o código de status HTTP 200, indicando sucesso.
        self.send_response(200)
        # Informa ao cliente que o conteúdo retornado será HTML.
        self.send_header("Content-type", "text/html; charset=utf-8")
        # Finaliza os cabeçalhos da resposta.
        self.end_headers()
        # Cria a página HTML que será enviada ao navegador.
        response = b"<html><body><h1>Hello World</h1></body></html>"
        # Escreve a resposta no fluxo de saída do servidor.
        self.wfile.write(response)

    # Sobrescreve o método que registra mensagens de log do servidor.
    # Como não queremos logs no console, ele simplesmente não faz nada.
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