from src.sorts.abstract_sorting_algorithm import AbstractSortingAlgorithm, T, Any, Callable


class CountingSort(AbstractSortingAlgorithm):
    def sort(self, array: list[T], key: Callable[[T], Any] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
        if cmp is not None:
            raise TypeError("This algorithm doesn't require compare function")

        if key is None:
            key = lambda x : x

        new_array = self.prepare_with_key(array, key)

        if new_array is None:
            return array

        if len(new_array) <= 1:
            return new_array
        return self.rebuild(self.count(new_array))

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

    def prepare_with_key(self, array: list[int], key) :
        new_array = [key(x) for x in array]
        for element in new_array:
            if element < 0:
                return None
        return new_array

if __name__ == "__main__":
    print(CountingSort().sort([0]))