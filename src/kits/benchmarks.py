import time
from typing import Callable

from tabulate import tabulate

from src.kits.generator_cases import GeneratorTestCases
from src.sorts.bubble_sort import BubbleSort
from src.sorts.bucket_sort import BucketSort
from src.sorts.counting_sort import CountingSort
from src.sorts.heap_sort import HeapSort
from src.sorts.insertion_sort import InsertionSort
from src.sorts.quick_sort import QuickSort
from src.sorts.radix_sort import RadixSort
from src.sorts.selection_sort import SelectionSort


def timeit_once(func, *agrs, **kwargs):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        result_time = time.perf_counter() - start
        return result, result_time
    return wrapper

def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    result = {}
    for name_array, value_array in arrays.items():
        result[name_array] = {}
        for name_algorithm, algorithm in algos.items():
            timed_sort = timeit_once(algorithm)
            result[name_array][name_algorithm] = timed_sort(value_array)[1]

    return result

def generate_markdown_table(benchmarks_results: list[dict[str, dict[str, float]]]) -> None:
    full_report = "# Отчет по бенчмаркам алгоритмов сортировки\n\n"

    for test_case_dict_of_dicts, count in benchmarks_results:
        list_of_dict_results = []

        for array_type, times_dict in test_case_dict_of_dicts.items():
            row_dict = {"Тип массива": array_type}
            for algo_name, time_value in times_dict.items():
                row_dict[algo_name] = f"{time_value:.4f}s"
            list_of_dict_results.append(row_dict)

        markdown_table = tabulate(list_of_dict_results, headers="keys", tablefmt="pipe")

        full_report += f"## Количество элементов: {count}\n\n"
        full_report += markdown_table
        full_report += "\n\n"

    return full_report

def create_markdown_report(max_exponent: int):
    algorithms_for_comparison = {
        "Bubble Sort": BubbleSort().sort,
        "Selection Sort": SelectionSort().sort,
        "Insertion Sort": InsertionSort().sort,
        "Quick Sort": QuickSort().sort,
        "Heap Sort": HeapSort().sort,
        "Bucket Sort": BucketSort().sort

    }
    algorithms_for_counting = {
        "Counting Sort": CountingSort().sort,
        "Radix Sort": RadixSort().sort,
        "Bucket Sort": BucketSort().sort
    }
    count_elements = [10 ** i for i in range(1, max_exponent + 1)]

    result_of_dicts = []

    for count in count_elements:
        seed = count
        arrays = {
            "Nearly sorted 10%" : GeneratorTestCases.nearly_sorted(count, int(count * 0.1), user_seed=seed**2),
            "Nearly sorted 20%" : GeneratorTestCases.nearly_sorted(count, int(count * 0.2), user_seed=seed**2),
            "Nearly sorted 30%" : GeneratorTestCases.nearly_sorted(count, int(count * 0.3), user_seed=seed**2),
            "Nearly sorted 40%" : GeneratorTestCases.nearly_sorted(count, int(count * 0.4), user_seed=seed**2),
            "Nearly sorted 50%" : GeneratorTestCases.nearly_sorted(count, int(count * 0.5), user_seed=seed**2),
            "Rand int array"    : GeneratorTestCases.rand_int_array(count, 0, count - 1, user_seed=seed**2),
            "Many duplicates"   : GeneratorTestCases.many_duplicates(count, int(count * 0.5), user_seed=seed**2),
            "Reverse sorted"    : GeneratorTestCases.reverse_sorted(count),
            "Rand float array"  : GeneratorTestCases.rand_float_array(count, count * 0.5, count * 0.95, user_seed=seed**2)
        }
        result_of_dicts.append((benchmark_sorts(arrays, algorithms_for_comparison), count))

    with open("benchmarks.md", mode="w") as report:
        report.write(generate_markdown_table(result_of_dicts))

create_markdown_report(4)