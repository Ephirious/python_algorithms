import pytest

from src.functions.factorial import Factorial
from src.functions.fibonacci import Fibonacci

factorial_test_cases = [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (10, 3628800),
    (20, 2432902008176640000)
]
@pytest.mark.parametrize("n, result", factorial_test_cases)
def test_factorial_positive(n, result):
    factorial = Factorial()
    assert factorial.iterative(n) == result
    assert factorial.recursive(n) == result

fibonacci_test_cases = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (20, 6765)
]
@pytest.mark.parametrize("n, result", fibonacci_test_cases)
def test_fibonacci_positive(n, result):
    fibonacci = Fibonacci()
    assert fibonacci.iterative(n) == result
    assert fibonacci.recursive(n) == result