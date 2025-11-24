from abc import ABC, abstractmethod
from typing import Callable, Any, TypeVar

T = TypeVar("T")

class AbstractSortingAlgorithm(ABC):
    @abstractmethod
    def sort(self, array: list[T], key: Callable[[T], Any] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
        pass

    def compare_function(self, key: Callable[[T], Any] | None = None, cmp: Callable[[T, T], int] | None = None):
        if key is not None and cmp is not None:
            raise TypeError("Cannot specify both 'key' and 'cmp' arguments")

        compare_function = lambda a, b: a > b
        if key is not None:
            compare_function = lambda a, b: key(a) > key(b)
        elif cmp is not None:
            compare_function = lambda a, b: cmp(a, b) > 0

        return compare_function