from src.sorts.abstract_sorting_algorithm import AbstractSortingAlgorithm, T, Any, Callable


class InsertionSort(AbstractSortingAlgorithm):
    def sort(self, array: list[T], key: Callable[[T], Any] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
        compare_function = self.compare_function(key, cmp)
        copy = array.copy()
        for i in range(1, len(copy)):
            j = i - 1
            while j >= 0 and compare_function(copy[j], copy[i]):
                copy[i], copy[j] = copy[j], copy[i]
                j -= 1
                i -= 1
        return copy