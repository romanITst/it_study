#!/usr/bin/env python3

# Description: This script is shows how the "function"
#  should be look. 
print("Enter the 1st number: ")
a = int(input())

print("Enter the 2nd number: ")
b = int(input())

def example(a, b):

    '''
    Sum 2 numbers and return the result
    :param a: 1st number
    :param b: 2nd number
    :return: the sum of a & b
    '''
    return a + b

result = example(a, b)
print(f"The sum of {a} & {b} is {result}")

