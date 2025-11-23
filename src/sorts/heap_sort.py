from src.sorts.abstract_sorting_algorithm import AbstractSortingAlgorithm


class HeapSort(AbstractSortingAlgorithm):
    def sort(self, array: list[int]) -> list[int]:
        copy = array.copy()

        for i in range(len(copy) // 2 - 1, -1, -1):
            self.sift_down(copy, len(copy), i)

        for i in range(len(copy) - 1, 0, -1):
            copy[0], copy[i] = copy[i], copy[0]
            self.sift_down(copy, i, 0)

        return copy

    def sift_down(self, array: list[int], size: int, i: int):
        while True:
            index_largest = i
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < size and array[index_largest] < array[left_index]:
                index_largest = left_index
            if right_index < size and array[index_largest] < array[right_index]:
                index_largest = right_index

            if index_largest != i:
                array[index_largest], array[i] = array[i], array[index_largest]
                i = index_largest
            else:
                break