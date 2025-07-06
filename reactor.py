from .demultiplexer import Demultiplexer


class Reactor:
    def __init__(self, event_handler: IEventHandler, selector: BaseSelector):
        self._init_selector()

    def _init_selector(self):
        self.selector = selectors.DefaultSelector()
        self.selector.register(
            event_handler.fd,
            selector.EVENT_READ,
            event_handler.accept
        )

    def start(self):
        while True:
            events = self.selector.select()
            for key, event_mask in events:
                key.data(key.fileobj)
