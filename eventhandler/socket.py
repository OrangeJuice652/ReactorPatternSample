from .i_event_handler import IEventHandler
import socket
import os


class SocketEventHandler(IEventHandler):
    def __init__(self) -> None:
        self._init_socket()

    def _init_socket(self):
        self._socket = socket.socket()
        self._socket.bind(
            (
                os.getenv('SOCKET_HOST'),
                os.getenv('SOCKET_PORT')
            )
        )
        self._socket.setblocking(False)
        self._socket.listen()

    @property
    def file_descriptor(self):
        return self._socket

    @property
    def handle(self, file_descriptor):
        connect, address = file_descriptor.accept()
        connect.setblocking(False)
        # reactorに登録

