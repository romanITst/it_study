#!/usr/bin/env python3 

# Description: This script shows how to use keyword arguments.


def create_person_info(name, age, city):
    '''
    Create a person's information string
    :param name: person's name
    :param age: person's age
    :param city: person's city
    :return: A string containing the person's information
    '''
    info = f"{name}, {age}, {city}"
    return info

person_info = create_person_info(name="Roman", age="23", city="Gomel")
print(person_info)
