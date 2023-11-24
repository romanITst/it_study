#!/usr/bin/env python3

# Description: This script shows how to use *args with strings.

def strings(*args):
    result = ""
    for s in args:
        result += s
    return result
    
result2 = strings("Hello, ", "Dev", "Ops", "!")
print(result2)

