import selectors
from typing import Callable


class Demultiplexer:
    def __init__(self, handle: Handle, accept_func: Callable):
        self.selector = selectors.DefaultSelector()
        self.selector.register(
                        handle.handler,
            selector.EVENT_READ,
            accept_func
        )

    def register(self, accept_func: Callable):
        self.selector.register(
            
        )
