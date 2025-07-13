from abc import ABC, abstractmethod
from typing import Any


class IEventHandler(ABC):
    @property
    @abstractmethod
    def file_descriptor(self) -> Any:
        pass

    @property
    @abstractmethod
    def handle(self) -> Any:
        pass

