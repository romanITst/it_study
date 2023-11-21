#!/usr/bin/env python3

# Description: This script shows how to use *args in functions

def add_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result

result2 = add_numbers(1, 2, 3, 4, 5)
print(result2)