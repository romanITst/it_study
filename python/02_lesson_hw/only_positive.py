#!/usr/bin/env python3


# Description: 
#
#


total = 0

while True:
    num = int(input("Put the positive integer: "))
    if num <= -1:
        print ("You should to put only POSITIVE integers. Exit")
        break
    total += num
    print ("Sum:", total)