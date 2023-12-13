#!/usr/bin/env python3

# Description: This script shows how to use dictionary methods.


person = {"name": "Roman", "age": 23, "county": "Belarus"}

keys = person.keys()
values = person.values()
items = person.items()

print(keys)
print(values)
print(items)

person["occupation"] = "Builder"

removed_item = person.pop("age")

print(person)
print(removed_item)

