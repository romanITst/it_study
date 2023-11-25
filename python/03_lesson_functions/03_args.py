#!/usr/bin/env python3

# Description: This script shows how to use *args in functions


def numbers(*args):
    '''
    Sum the numbers
    :param args: List of numbers
    :return: Sum of this numbers
    '''
    result = 0
    for num in args:
        result += num
    return result

result2 = numbers(1, 3, 3, 7)
print(f"Sum: {result2}")