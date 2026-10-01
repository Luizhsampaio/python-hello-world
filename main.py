from server_factory import create_server


if __name__ == "__main__":
    server = create_server(port=80)
    print("Servidor rodando em http://localhost")
    print("Rotas disponíveis:")
    print(" - http://localhost/")
    print(" - http://localhost/1")
    print(" - http://localhost/2")
    server.serve_forever()
