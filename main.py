from reactor import Reactor
from eventhandler import (
    ListnerSocket,
    EchoSocket,
)


if __name__ == "__main__":
    reactor = Reactor(
        ListnerSocket()
    )
    for result in reactor.event_loop():
        if isinstance(result, EchoSocket):
            if result.should_close:
                reactor.unregist_event_handler(
                    result
                )
                del result
            else:
                # regist echo socket for the reactor
                reactor.regist_new_event_handler(
                    result
                )

