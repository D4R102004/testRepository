from typing import Tuple
# This allows for user to input values in accordance with whatever supported types in this class
from Utilities import utilities


def is_peak(input_list: list[int], i: int) -> bool:
    if i == 0 or i == len(input_list) - 1:
        return False
    return input_list[i - 1] < input_list[i] > input_list[i + 1]


def is_valley(input_list: list[int], i: int) -> bool:
    if i == 0 or i == len(input_list) - 1:
        return False
    return input_list[i - 1] > input_list[i] < input_list[i + 1]


def peaks_valleys_getter(input_list: list[int]) -> Tuple[list[Tuple[int, int]], list[Tuple[int, int]]]:
    peaks = []
    valleys = []
    for i in range(1, len(input_list) - 1):
        if is_peak(input_list, i):
            peaks.append((i, input_list[i]))
        elif is_valley(input_list, i):
            valleys.append((i, input_list[i]))
    return peaks, valleys


tests = utilities.UserInput.get_input("Enter number of tests: ", int)
while tests > 0:
    print(f"Remaining tests: {tests}")
    numbers = utilities.UserInput.cycle_get_input("Enter a value: ", float)
    peak_numbers, valley_numbers = peaks_valleys_getter(numbers)
    print(f'Index of Peak numbers and numbers: {peak_numbers}')
    print(f'Index of Valley numbers and numbers: {valley_numbers}')
    tests -= 1