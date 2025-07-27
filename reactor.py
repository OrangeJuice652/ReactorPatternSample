from typing import List, Tuple
import selectors
from eventhandler import IEventHandler


class Reactor:
    def __init__(self, event_handler: IEventHandler):
        self._init_selector(
            event_handler
       )

    def _init_selector(self, event_handler: IEventHandler):
        self.selector  = selectors.DefaultSelector()
        self.selector.register(
            fileobj=event_handler.file_descriptor,
            events=selectors.EVENT_READ,
            data=event_handler,
        )

    def regist_new_event_handler(self, event_handler: IEventHandler):
        self.selector.register(
            fileobj=event_handler.file_descriptor,
            events=selectors.EVENT_READ,
            data=event_handler,
        )

    def unregist_event_handler(self, event_handler: IEventHandler):
        self.selector.unregister(
            fileobj=event_handler.file_descriptor,
        )

    def event_loop(self):
        while True:
            events: List[Tuple[selectors.SelectorKey, selectors._EventMask]] = self.selector.select()
            for key, _ in events:
                yield key.data.handle(key.fileobj)

