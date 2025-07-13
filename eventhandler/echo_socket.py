from .i_event_handler import IEventHandler
from socket import socket
from typing import Any


class EchoSocket(IEventHandler):
    def __init__(self, socket: socket):
        self._socket = socket
        self._socket.setblocking(False)

    @property
    def file_descriptor(self) -> Any:
        return self._socket

    @property
    def handle(self) -> Any:
        pass

