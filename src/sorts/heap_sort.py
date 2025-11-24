from src.sorts.abstract_sorting_algorithm import AbstractSortingAlgorithm, T, Any, Callable



class HeapSort(AbstractSortingAlgorithm):
    def sort(self, array: list[T], key: Callable[[T], Any] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
        compare_function = self.compare_function(key, cmp)
        copy = array.copy()

        for i in range(len(copy) // 2 - 1, -1, -1):
            self.sift_down(copy, len(copy), i, compare_function)

        for i in range(len(copy) - 1, 0, -1):
            copy[0], copy[i] = copy[i], copy[0]
            self.sift_down(copy, i, 0, compare_function)

        return copy

    def sift_down(self, array: list[int], size: int, i: int, cmp):
        while True:
            index_largest = i
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < size and cmp(array[left_index], array[index_largest]):
                index_largest = left_index
            if right_index < size and cmp(array[right_index], array[index_largest]):
                index_largest = right_index

            if index_largest != i:
                array[index_largest], array[i] = array[i], array[index_largest]
                i = index_largest
            else:
                break