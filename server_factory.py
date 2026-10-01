from http.server import HTTPServer

from hello_world_handlers import HelloWorldHandler01, HelloWorldHandler02


def create_servers():
    server_01 = HTTPServer(("0.0.0.0", 8001), HelloWorldHandler01)
    server_02 = HTTPServer(("0.0.0.0", 8002), HelloWorldHandler02)
    return server_01, server_02
