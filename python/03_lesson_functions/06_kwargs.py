#!/usr/bin/env python3

# Description: shows how to use kwargs in functions

def display_info(**kwargs):
    '''
    Display information about person.
    :param kwargs: kwarg representing person's attributes.'''
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display = display_info(name="Roman", age=23, city="Gomel")
print(display)

