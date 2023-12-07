#!/usr/bin/env python3

# Description: This script organizes files in directory
# in connection with their .extensions - creates subdirs
# based on files .extensions


import os
import sys

def get_list_of_files(main_path):
    '''
    This function returns file names
    in dir you entered
    '''
    for foldername, subfolders, filenames in os.walk(main_path):
        return filenames
    return filenames

list_of_files = get_list_of_files(str(sys.argv[1]))

def get_file_extension(file_name):
    '''
    This script returns file extension
    '''
    file_name_wout_point = file_name.replace(".", " ")
    splitted_file_name = file_name_wout_point.split()
    file_extension = splitted_file_name[-1]
    return file_extension

def get_list_of_unique_extensions(list_of_files):
    '''
    This script returns list of
    unique extensions in dir
    '''
    list_of_extensions = []
    for files in list_of_files:
        list_of_extensions.append(get_file_extension(files))
    list_of_unique_extensions = []
    unique_extensions = set(list_of_extensions)
    for exts in unique_extensions:
        list_of_unique_extensions.append(exts)
    return list_of_unique_extensions

def creating_folder(folder_name):
    os.mkdir(folder_name)
    return folder_name

def creating_folders_by_extensions(unique_extensions):
    list_of_files = get_list_of_files(main_path=str(sys.argv[1]))
    unique_extensions = get_list_of_unique_extensions(list_of_files)
    list_of_created_folders = []
    for exts in unique_extensions:
        created_folder = creating_folder("folder.{}".format(exts))
        list_of_created_folders.append(created_folder)
    return list_of_created_folders

unique_extensions = get_list_of_unique_extensions(list_of_files)

print(creating_folders_by_extensions(unique_extensions))
    
