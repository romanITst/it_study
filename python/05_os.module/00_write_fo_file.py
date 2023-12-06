#!/usr/bin/env python3

# Description: This script is opening file (or creating if it doesn't exist)
# and writing to it needed information.


def opening_file():
    file_name = str(input("Enter the name of the file: "))
    with open(file_name, "w") as file_name:
        print("File is ready to writing")

opening_file()