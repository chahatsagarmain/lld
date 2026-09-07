from __future__ import annotations
from abc import abstractmethod , ABC

class HandlerInterface(ABC):

    def __init__(self):
        self._next_handler: HandlerInterface | None = None

    def set_next(self, handler: HandlerInterface | None) -> HandlerInterface | None:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, req: dict):
        pass 

class Handler1(HandlerInterface):
    
    def handle(self, req: dict):
        if "req1" in req:
            print(f"handling req at req1")
        elif self._next_handler is not None:
            self._next_handler.handle(req)
        else:
            print("Request unhandled at the end of the chain")

class Handler2(HandlerInterface):
    
    def handle(self, req: dict):
        if "req2" in req:
            print(f"handling req at req2")
        elif self._next_handler is not None:
            self._next_handler.handle(req)
        else:
            print("Request unhandled at the end of the chain")

class Handler3(HandlerInterface):

    def handle(self, req: dict):
        if "req3" in req:
            print(f"handling req at req3")
        elif self._next_handler is not None:
            self._next_handler.handle(req)
        else:
            print("Request unhandled at the end of the chain")
