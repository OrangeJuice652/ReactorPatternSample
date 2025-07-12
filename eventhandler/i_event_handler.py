from abc import ABC, abstractmethod


class IEventHandler(ABC):
    @property
    @abstractmethod
    def file_descriptor(self):
        pass

    @property
    @abstractmethod
    def handle(self):
        pass

