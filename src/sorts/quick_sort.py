from src.sorts.abstract_sorting_algorithm import AbstractSortingAlgorithm


class QuickSort(AbstractSortingAlgorithm):
    def sort(self, array: list[int]) -> list[int]:
        copy = array.copy()
        self._recursion_sort(copy, 0, len(copy) - 1)
        return copy

    def _recursion_sort(self, array: list[int], left: int, right: int):
        if right <= left:
            return

        pivot_index = self._get_median_of_three(array, left, right)
        array[left], array[pivot_index] = array[pivot_index], array[left]

        partition = self._partition(array, left, right, array[left])
        array[left], array[partition] = array[partition], array[left]
        self._recursion_sort(array, left, partition - 1)
        self._recursion_sort(array, partition + 1, right)



    def _partition(self, array: list[int], left: int, right: int, pivot: int) -> int:
        left_ptr = left
        right_ptr = right + 1
        while True:
            while left_ptr < right:
                left_ptr += 1
                if array[left_ptr] > pivot:
                    break
            while right_ptr > left:
                right_ptr -= 1
                if array[right_ptr] < pivot:
                    break
            if left_ptr >= right_ptr:
                return right_ptr
            array[left_ptr], array[right_ptr] = array[right_ptr], array[left_ptr]

    def _get_median_of_three(self, array: list[int], left: int, right: int) -> int:
        first = array[left], left
        mid = array[(left + right) // 2], ((left + right) // 2)
        last = array[right], right

        if first > mid:
            first, mid = mid, first
        if mid > last:
            mid, last = last, mid
        if first > mid:
            first, mid = mid, first

        return mid[1]
