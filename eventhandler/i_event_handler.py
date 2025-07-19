from abc import ABC, abstractmethod
from typing import Any


class IEventResult:
    pass
    

class IEventHandler(ABC):
    @property
    @abstractmethod
    def file_descriptor(self) -> Any:
        pass

    @property
    @abstractmethod
    def handle(self, *args) -> Any:
        pass

