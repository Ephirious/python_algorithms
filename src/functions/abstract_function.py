from abc import ABC, abstractmethod

class AbstractFunction(ABC):
    @abstractmethod
    def iterative(self, *args):
        pass

    @abstractmethod
    def recursive(self, *args):
        pass