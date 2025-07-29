from abc import ABC, abstractmethod

class BaseDetector(ABC):
    @abstractmethod
    def process_line(self, line: str):
        pass
