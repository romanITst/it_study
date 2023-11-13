#!/usr/bin/env python3

# Description:
#
#


try:    # result 'try'
    num1 = int(input("Enter the number you want to divide: "))
    num2 = int(input("Enter the number you want to divide by: "))
except ValueError:
    print ("Invalid input. You should to use only numbers.")
    print ("Try again")
    exit()
else:
    result = num1 / num2


try:    # result 'try'
    result = num1 / num2
except ZeroDivisionError:
    print ("Division by zero is not allowed. Do NOT use '0'")
else:
    print ("Your answer for division: ", result)