from random import Random

class GeneratorTestCases:
    @staticmethod
    def rand_int_array(number_of_elements: int,
                       lower_bound: int,
                       upper_bound: int,
                       *,
                       distinct = False,
                       user_seed = None
                       ) -> list[int]:
        if lower_bound >= upper_bound:
            raise ValueError("Incorrect lower and upper bounds")

        random_generator = Random(user_seed)
        if distinct:
            if (upper_bound - lower_bound + 1) < number_of_elements:
                raise ValueError("The range is too small for unique numbers")
            available_numbers = range(lower_bound, upper_bound + 1)
            return random_generator.sample(available_numbers, number_of_elements)
        return [random_generator.randint(lower_bound, upper_bound) for _ in range(number_of_elements)]

    @staticmethod
    def nearly_sorted(number_of_elements: int, swaps: int, *, user_seed = None) -> list[int]:
        new_array = list(range(number_of_elements))

        if number_of_elements < 2:
            return new_array

        random_generator = Random(user_seed)

        for i in range(swaps):
            from_index = random_generator.randint(0, number_of_elements - 1)

            while True:
                to_index = random_generator.randint(0, number_of_elements - 1)
                if to_index != from_index:
                    break
            new_array[from_index], new_array[to_index] = new_array[to_index], new_array[from_index]

        return new_array

    @staticmethod
    def many_duplicates(number_of_elements: int, k_unique=5, *, user_seed=None) -> list[int]:
        if k_unique <= 1:
            raise ValueError("Unique elements must be  1")

        unique_elements = list(range(k_unique))
        random_generator = Random(user_seed)
        return random_generator.choices(unique_elements, k = number_of_elements)

    @staticmethod
    def reverse_sorted(number_of_elements: int) -> list[int]:
        return list(range(number_of_elements, 0, -1))

    @staticmethod
    def rand_float_array(number_of_elements: int, lower_bound=0.0, upper_bound=1.0, *, user_seed=None) -> list[float]:
        if lower_bound >= upper_bound:
            raise ValueError("Incorrect lower and upper bounds")

        random_generator = Random(user_seed)

        return [random_generator.uniform(lower_bound, upper_bound) for _ in range(number_of_elements)]
