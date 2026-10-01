from http.server import HTTPServer

from hello_world_handlers import HelloWorldRouterHandler


def create_server(host: str = "0.0.0.0", port: int = 80) -> HTTPServer:
    return HTTPServer((host, port), HelloWorldRouterHandler)
