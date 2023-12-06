#!/usr/bin/env python3

# Description: This script is opening file (or creating if it doesn't exist)
# and writing to it information you need.


import sys


file_name = sys.argv[1]

def opening_and_writing_to_file(file_name):
    with open(file_name, "a+") as file:
        print("File is ready to writing")
        for i in range(int(sys.argv[3])):
            file.write(str(sys.argv[2]))
            file.write("\n")
    file.close()
    print("Information was added to file")

opening_and_writing_to_file(file_name)