from threading import Event, Thread

from server_factory import create_servers


if __name__ == "__main__":
    server_01, server_02 = create_servers()

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
