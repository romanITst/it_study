#!/usr/bin/env python3

# Description: This script helps you to know, who you are.
# Just enter your age to the command line and it will
# say, who you are: child, teenager or an adult. Enjoy

age = int(input("Enter your age: "))

if age <= 12:
    print (f"Your age is {age}. You are a child.")
elif age <= 19:
    print (f"Your age is {age}. You are a teenager.")
else:
    print (f"Your age is {age}. You are an adult.")