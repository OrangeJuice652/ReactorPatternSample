from .i_event_handler import IEventHandler
from .echo_socket import EchoSocket
from socket import socket as Socket
import os


class ListnerSocket(IEventHandler):
    def __init__(self) -> None:
        self._init_socket()

    def __del__(self):
        self._socket.close()

    def _init_socket(self):
        self._socket = Socket()
        self._socket.bind(
            (
                os.getenv('SOCKET_HOST'),
                int(os.getenv('SOCKET_PORT')),
            )
        )
        self._socket.setblocking(False)
        self._socket.listen()

    @property
    def file_descriptor(self):
        return self._socket

    def handle(self, *args):
        if len(args) > 0 and isinstance(
            file_descriptor:=args[0],
            Socket
        ):
            socket, address = file_descriptor.accept()
            return EchoSocket(socket, address)

