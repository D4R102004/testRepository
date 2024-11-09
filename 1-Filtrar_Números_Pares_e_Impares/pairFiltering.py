from typing import Tuple, Callable, Any
# This allows for user to input values in accordance with whatever supported types in this class
from Utilities import utilities


def is_even(number: int) -> bool:
    return number % 2 == 0


def is_odd(number: int) -> bool:
    return number % 2 != 0


def parity_filter(input_list: list[int]) -> Tuple[list[int], list[int]]:
    # Filterer method is defined for a set of n properties, to return a dictionary
    # with references to lists that contain all elements that fulfill said properties
    filterer = utilities.ListUtils.filter_by_conditions(input_list, is_even, is_odd)
    even_numbers_list = filterer.get(is_even.__name__)
    odd_numbers_list = filterer.get(is_odd.__name__)
    return even_numbers_list, odd_numbers_list


# Write how many tests you want to make.
tests = utilities.UserInput.get_input("Enter number of tests: ", int)
while tests > 0:
    print(f"Remaining tests: {tests}")
    numbers = utilities.UserInput.cycle_get_input("Enter a value: ", int)
    even_numbers, odd_numbers = parity_filter(numbers)
    print(f'Even numbers: {even_numbers}')
    print(f'Odd numbers: {odd_numbers}')
    tests -= 1
