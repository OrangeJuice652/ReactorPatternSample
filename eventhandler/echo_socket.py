from .i_event_handler import IEventHandler
from socket import socket
from typing import Any


class EchoSocket(IEventHandler):
    def __init__(self, socket: socket, address):
        self._socket = socket
        self._address = address
        self.should_close = False
        self._socket.setblocking(False)

    def __del__(self):
        self._socket.close()

    @property
    def file_descriptor(self) -> Any:
        return self._socket

    @property
    def handle(self, *_) -> Any:
        data = self._socket.recv(1000)  # Should be ready
        if data:
            print('echoing', repr(data), 'to', self._socket)
            self._socket.send(data)  # Hope it won't block
            return None
        else:
            print('closing', self._socket)
            self.should_close = True
            return self

