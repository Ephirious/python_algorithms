from src.sorts.abstract_sorting_algorithm import AbstractSortingAlgorithm, T, Any, Callable


class BubbleSort(AbstractSortingAlgorithm):
    def sort(self, array: list[T], key: Callable[[T], Any] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
        compare_function = self.compare_function(key, cmp)

        copy = array.copy()

        for i in range(len(copy) - 1):
            for j in range(i + 1, len(copy)):
                if compare_function(copy[i], copy[j]):
                    copy[i], copy[j] = copy[j], copy[i]

        return copy