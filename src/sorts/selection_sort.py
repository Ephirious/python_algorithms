from src.sorts.abstract_sorting_algorithm import AbstractSortingAlgorithm, T, Any, Callable

class SelectionSort(AbstractSortingAlgorithm):
    def sort(self, array: list[T], key: Callable[[T], Any] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
        compare_function = self.compare_function(key, cmp)
        copy = array.copy()

        for i in range(len(copy) - 1):
            min_index = i
            for j in range(i + 1, len(copy)):
                if compare_function(copy[min_index], copy[j]):
                    min_index = j
            copy[min_index], copy[i] = copy[i], copy[min_index]

        return copy