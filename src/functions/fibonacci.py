from src.functions.abstract_function import AbstractFunction


class Fibonacci(AbstractFunction):
    def iterative(self, n: int) -> int:
        self.check_argument(n)
        if n == 0:
            return 0
        elif n == 1:
            return 1

        prev = 0
        next = 1
        for i in range(1, n):
            prev, next = next, prev + next
        return next

    def recursive(self, n: int) -> int:
        self.check_argument(n)
        return self._recursive(n)

    def check_argument(self, n: int) -> None:
        if not isinstance(n, int):
            raise TypeError("For factorial function argument must be integer")
        if n < 0:
            raise ValueError("For factorial function argument must be >= 0")

    def _recursive(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        return self._recursive(n - 1) + self._recursive(n - 2)
