from src.sorts.abstract_sorting_algorithm import AbstractSortingAlgorithm


class BubbleSort(AbstractSortingAlgorithm):
    def sort(self, array: list[int]) -> list[int]:
        copy = array.copy()
        for i in range(len(copy) - 1):
            for j in range(i + 1, len(copy)):
                if copy[i] > copy[j]:
                    copy[i], copy[j] = copy[j], copy[i]

        return copy