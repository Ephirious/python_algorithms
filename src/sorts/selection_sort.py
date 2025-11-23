from src.sorts.abstract_sorting_algorithm import AbstractSortingAlgorithm


class SelectionSort(AbstractSortingAlgorithm):
    def sort(self, array: list[int]) -> list[int]:
        copy = array.copy()

        for i in range(len(copy) - 1):
            min_index = i
            for j in range(i + 1, len(copy)):
                if copy[min_index] > copy[j]:
                    min_index = j
            copy[min_index], copy[i] = copy[i], copy[min_index]

        return copy