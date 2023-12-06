#!/usr/bin/env python3

# Description: This script is opening file (or creating if it doesn't exist)
# and writing to it information you need. 


import sys
import os


def main_function(file_name):
    with open(file_name, "a+") as file:
        for i in range(int(sys.argv[3])):
            file.write(str(sys.argv[2]))
            file.write("\n")
    file.close()
    print("Text was added to file!")


if os.path.exists(str(sys.argv[1])) == True:
    print("File is exist! Writing text to a file...")
    main_function(str(sys.argv[1]))
    
if os.path.exists(str(sys.argv[1])) == False:
    print("The file is doesn't exist. Want to create it? Type 'y' or 'n'")
    if str(input()) == "y":
        main_function(str(sys.argv[1]))
        sys.exit()
    else:
        print("Exit...")
        sys.exit()


