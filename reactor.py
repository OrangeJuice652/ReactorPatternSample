from typing import List, Tuple
import selectors


class Reactor:
    def __init__(self, event_handler: IEventHandler):
        self._init_selector(event_handler: IEventHandler)

    def _init_selector(self, event_handler):
        self.selector  = selectors.DefaultSelector()
        self.selector.register(
            fileobj=event_handler.fd,
            events=selectors.EVENT_READ,
            data=event_handler.accept,
        )

    def start(self):
        while True:
            events: List[Tuple[selectors.SelectorKey, selectors._EventMask]] = self.selector.select()
            for key, _ in events:
                key.data(key.fileobj)

