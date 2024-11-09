# This allows user to input values in accordance with whatever supported types in this class
from Utilities import utilities
import sys


def negative_order_filter(input_list: list[int]) -> list[int]:
    negative_numbers = [item for item in input_list if item < 0]
    return sorted(negative_numbers)


tests = utilities.UserInput.get_input("Enter number of tests: ", int)
while tests > 0:
    print(f"Remaining tests: {tests}")
    numbers = utilities.UserInput.cycle_get_input("Enter a value: ", int)
    sorted_negatives = negative_order_filter(numbers)
    print(sorted_negatives)
    tests -= 1
