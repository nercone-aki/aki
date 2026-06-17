from kaede import Request, Response, WebSocket, Callback
from typing import Literal, Callable
from .routing import Router

class Aki(Callback):
    def __init__(self):
        super().__init__()
        self.router = Router()

    async def on_request(self, request: Request) -> Response:
        return await self.router.dispatch(request, ws=None)

    async def on_websocket(self, request: Request, ws: WebSocket):
        await self.router.dispatch(request, ws=ws)

    def add_route(self, path: str, *, methods: list[Literal["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]] | None = None, callback: Callable) -> Callable:
        return self.router.add_route(path, methods=methods, callback=callback)

    def route(self, path: str, *, methods: list[Literal["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]] | None = None) -> Callable:
        return self.router.route(path, methods=methods)
