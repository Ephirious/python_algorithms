import pytest

from src.sorts.bubble_sort import BubbleSort
from src.sorts.bucket_sort import BucketSort
from src.sorts.counting_sort import CountingSort
from src.sorts.heap_sort import HeapSort
from src.sorts.insertion_sort import InsertionSort
from src.sorts.quick_sort import QuickSort
from src.sorts.radix_sort import RadixSort
from src.sorts.selection_sort import SelectionSort


@pytest.mark.parametrize(
    "array",
    [
        [],
        [0],
        [-1],
        [42],
        [1, 2],
        [2, 1],
        [0, 0],
        [5, 5, 5, 5],
        [1, 1, 2, 2, 1, 2],
        [3, 1, 4, 1, 5, 9, 2, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [-5, -2, 0, 3, 10],
        [-10, -5, 0, 5, 10],
        [-1, -1, 0, 1, 1],
        [-3, -1, -4, -1, -5],
        [0, 0, 0],
        [1, 2, 4, 3, 5],
        [10, 20, 30, 25, 40, 50],
        [1, 100, 2, 99, 3, 98],
    ]
)
def test_sorts_algorithms_with_all_integers(array: list[int]):
    sorts_methods = [
        BubbleSort(),
        InsertionSort(),
        SelectionSort(),
        QuickSort(),
        HeapSort()
    ]
    for method in sorts_methods:
        assert method.sort(array) == sorted(array)

@pytest.mark.parametrize(
    "array",
    [
        [],
        [0],
        [42],
        [1, 2],
        [2, 1],
        [0, 0],
        [5, 5, 5, 5],
        [1, 1, 2, 2, 1, 2],
        [3, 1, 4, 1, 5, 9, 2, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [0, 0, 0],
        [1, 2, 4, 3, 5],
        [10, 20, 30, 25, 40, 50],
        [1, 100, 2, 99, 3, 98],
    ]
)
def test_sorts_algorithms_with_natural_numbers(array: list[int]):
    sorts_methods = [
        BubbleSort(),
        InsertionSort(),
        SelectionSort(),
        QuickSort(),
        CountingSort(),
        RadixSort(),
        BucketSort(),
        HeapSort()
    ]
    for method in sorts_methods:
        assert method.sort(array) == sorted(array)