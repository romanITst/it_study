#!/usr/bin/env python3

# Description: This script organizes files in directory
# in connection with their .extensions - creates subdirs
# based on files .extensions


import os
import sys

def get_list_of_files(main_path):
    for foldername, subfolders, filenames in os.walk(main_path):
        return filenames
    return filenames

list_of_files = get_list_of_files(str(sys.argv[1]))

def get_file_extension(file_name):
    file_name_wout_point = file_name.replace(".", " ")
    splitted_file_name = file_name_wout_point.split()
    file_extension = splitted_file_name[-1]
    return file_extension

def get_list_of_unique_extensions(list_of_files):
    list_of_extensions = []
    for files in list_of_files:
        list_of_extensions.append(get_file_extension(files))
    list_of_unique_extensions = []
    unique_extensions = set(list_of_extensions)
    for exts in unique_extensions:
        list_of_unique_extensions.append(exts)
    return list_of_unique_extensions

unique_extensions = get_list_of_unique_extensions(list_of_files)
print(unique_extensions)