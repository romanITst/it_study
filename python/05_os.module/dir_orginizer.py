#!/usr/bin/env python3

# Description: This script organizes files in directory
# in connection with their .extensions - creates subdirs
# based on files .extensions


import os
import sys

def get_list_of_file(main_path):
    for foldername, subfolders, filenames in os.walk(main_path):
        print("Filenames: ", filenames)
    return filenames

def get_file_extension(file_name):
    file_name_wout_point = file_name.replace(".", " ")
    splitted_file_name = file_name_wout_point.split()
    file_extension = splitted_file_name[-1]
    return file_extension


file_extension = get_file_extension("file02.txt")
print(file_extension)
    


#get_list_of_file(str(sys.argv[1]))