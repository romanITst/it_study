#!/usr/bin/env python3

# Description: This script is uses a 'for' loop
# to display all odd numbers from 1 to 50.

for i in range(1, 51):
    if i % 2 == 0:
        continue
    print (i)