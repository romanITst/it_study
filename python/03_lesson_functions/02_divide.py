#!/usr/bin/env python3

# Description: With this script you can divide the dividend by divider. 

print("To divide you should enter 2 integers one by one.")
dividend = int(input("Dividend: "))
divider = int (input("Divider: "))   
#number which user will enter will be ARGUMENT


def divide(dividend, divider): #PARAMETERS are: dividend & divider

    '''Divide the dividend by divisor
    param dividend: Number what will divide by divisor
    param divisor: Number by which dividend will divide
    return: The result of the division'''

    return dividend / divider

result = divide(dividend, divider) 
print(f"The result of division is: {result}")
