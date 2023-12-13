#!/usr/bin/env python3

# Description: This script shows how to use list methods.


fruits = ["grape", "banana", "orange"]

fruits.append("apple")
fruits.extend(["pearl", "melon", "manana"])
fruits.insert(1, "pear")
fruits.remove("banana")
removed_fruits = fruits.pop(2)

print(fruits)
print(removed_fruits)