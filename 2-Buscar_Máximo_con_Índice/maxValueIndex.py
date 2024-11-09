from typing import Tuple
# This allows user to input values in accordance with whatever supported types in this class
from Utilities import utilities


def max_index(input_list: list[int]) -> Tuple[int, int]:
    if not input_list:
        raise ValueError("Empty array")
    max_value, max_idx = input_list[0], 0
    for i in range(1, len(input_list)):
        if input_list[i] > max_value:
            max_value, max_idx = input_list[i], i
    return max_value, max_idx


tests = utilities.UserInput.get_input("Enter number of tests: ", int)
while tests > 0:
    print(f"Remaining tests: {tests}")
    numbers = utilities.UserInput.cycle_get_input("Enter a value: ", float)
    maximum_index = max_index(numbers)
    print(f"Max value: {maximum_index[0]}. \nIndex: {maximum_index[1]}")
    tests -= 1
