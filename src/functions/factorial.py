from src.functions.abstract_function import AbstractFunction


class Factorial(AbstractFunction):
    def iterative(self, n: int) -> int:
        self.check_argument(n)

        result = 1
        for i in range(1, n):
            result *= (i + 1)
        return result

    def recursive(self, n: int) -> int:
        self.check_argument(n)
        return self._recursive(n)


    def _recursive(self, n: int) -> int:
        if n <= 1:
            return 1
        return n * self._recursive(n - 1)

    def check_argument(self, n: int) -> None:
        if not isinstance(n, int):
            raise TypeError("For factorial function argument must be integer")
        if n < 0:
            raise ValueError("For factorial function argument must be >= 0")