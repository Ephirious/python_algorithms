from src.sorts.AbstractSortingAlgorithm import AbstractSortingAlgorithm


class CountingSort(AbstractSortingAlgorithm):
    def sort(self, array: list[int]) -> list[int]:
        if len(array) <= 1:
            return []
        return self.rebuild(self.count(array))

    def count(self, array: list[int]) -> list[int]:
        size = max(array) + 1
        temp_array = [0] * size
        for index in array:
            temp_array[index] += 1
        return temp_array

    def rebuild(self, counting_array) -> list[int]:
        size = len(counting_array)
        new_array = []
        for i in range(len(counting_array)):
            for j in range(counting_array[i]):
                new_array.append(i)
        return new_array

if __name__ == "__main__":
    print(CountingSort().sort([3, 1, 4, 1, 5, 9, 2, 6]))