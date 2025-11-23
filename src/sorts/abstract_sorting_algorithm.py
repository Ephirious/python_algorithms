from abc import ABC, abstractmethod

class AbstractSortingAlgorithm(ABC):
    @abstractmethod
    def sort(self, array: list[int]) -> list[int]:
        pass