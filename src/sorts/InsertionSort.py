from src.sorts.AbstractSortingAlgorithm import AbstractSortingAlgorithm

class InsertionSort(AbstractSortingAlgorithm):
    def sort(self, array: list[int]) -> list[int]:
        copy = array.copy()
        for i in range(1, len(copy)):
            j = i - 1
            while copy[i] < copy[j] and j >= 0:
                copy[i], copy[j] = copy[j], copy[i]
                j -= 1
                i -= 1
        return copy