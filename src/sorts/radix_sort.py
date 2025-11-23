from src.sorts.abstract_sorting_algorithm import AbstractSortingAlgorithm


class RadixSort(AbstractSortingAlgorithm):
    def sort(self, array: list[int], base: int = 10) -> list[int]:
        copy = array.copy()
        count = self.get_max_digits(copy)
        for i in range(count):
            sorting_array = [[] for _ in range(10)]
            for element in copy:
                index = (element // base ** i) % base
                sorting_array[index].append(element)
            copy = [x for inner in sorting_array for x in inner]

        return copy

    def get_max_digits(self, array: list[int]):
        maximum = 1
        for element in array:
            maximum = max(maximum, element)
        return self.get_count_digits(maximum)

    def get_count_digits(self, number: int):
        number = abs(number)
        if number == 0:
            return 1
        count = 0
        while number != 0:
            count += 1
            number //= 10
        return count


if __name__ == "__main__":
    obj = RadixSort()
    print(obj.sort([42]))