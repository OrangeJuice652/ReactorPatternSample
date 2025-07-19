from .reactor import Reactor
from .eventhandler import (
    ListnerSocket,
    EchoSocket,
)

            
def main():
    print("Hello from reactorpatternsample!")


if __name__ == "__main__":
    reactor = Reactor(
        ListnerSocket()
    )
    for result in reactor.event_loop():
        if isinstance(result, EchoSocket):
            # regist echo socket for the reactor
            reactor.regist_new_event_handler(
                result
            )
