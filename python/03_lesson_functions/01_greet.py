#!/usr/bin/env python3

# Description: It's shows how to use args in functions.

print("Hello. I'm Jarvis. You should to fill out the form. Your name: ")
name = str(input())

print("Your age: ")
age = str(input())

print("Your profession is: ")
profession = str(input())


def greet(name, age, profession):

    message = (f"Hi, {name}! Nice to meet you! You are {age} years old and you are {profession}. Right?")

    '''
    purpose: greet anybody
    param name: name
    param age: age
    param profession: profession
    return: Greeting anybody and ask about age and profession
    '''

    return message


result = greet(name, age, profession)
print(result)

 