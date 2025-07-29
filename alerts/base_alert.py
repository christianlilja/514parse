from abc import ABC, abstractmethod

class BaseAlert(ABC):
    @abstractmethod
    def send(self, message: str):
        pass
