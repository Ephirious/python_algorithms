from multiprocessing.connection import arbitrary_address

from src.sorts.abstract_sorting_algorithm import AbstractSortingAlgorithm
from src.sorts.quick_sort import QuickSort


class BucketSort(AbstractSortingAlgorithm):
    def sort(self, array: list[int | float], numberOfBuckets: int | None = None) -> list[int | float]:
        if len(array) <= 1:
            return array

        copy = array.copy()
        if numberOfBuckets is None:
            numberOfBuckets = int(len(copy) ** 0.5)

        maximum = max(copy)
        minimum = min(copy)
        array_range = maximum - minimum
        if maximum - minimum == 0:
            return copy

        buckets = [[] for _ in range(numberOfBuckets)]
        for element in copy:
            index = int((element - minimum) / array_range * (numberOfBuckets - 1))
            buckets[index].append(element)

        sort_object = QuickSort()
        copy = [x for inner in buckets for x in sort_object.sort(inner)]
        return copy

if __name__ == "__main__":
    bucket_obj = BucketSort()
    print(bucket_obj.sort([0.89, 0.56, 0.65, 0.12, 0.69, 0.21, 0.15, 0.45, 0.63, 0.36]))
    print(bucket_obj.sort([15, 8, 22, 5, 12, 35, 1, 19, 28, 42]))