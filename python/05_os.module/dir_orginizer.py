#!/usr/bin/env python3

# Description: This script organizes files in directory
# in connection with their .extensions - creates subdirs
# based on files .extensions.
# This script doesn't have dictionary with all existing 
# extensions. It's looks to last symbols after point in
# files name -> file.{txt} or file.xxx.ggg.{txt}
# input: ./dir_organizer.py path/to/dir


import os
import sys
import shutil


def get_list_of_files(main_path):
    '''
    This function returns file names
    in dir you entered
    '''
    for foldername, subfolders, filenames in os.walk(main_path):
        return filenames
    return filenames

print("Scanning...")
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

print("Getting list of extensions...")
unique_extensions = get_list_of_unique_extensions(list_of_files)

def creating_folder(folder_name):
    '''
    Creates folder.
    '''
    os.mkdir(folder_name)
    return folder_name


def creating_folders_by_extensions(unique_extensions):
    '''
    This function creates folders in connection with
    list of unique extensions and returns list of
    created folders.
    '''
    list_of_files = get_list_of_files(main_path=str(sys.argv[1]))
    unique_extensions = get_list_of_unique_extensions(list_of_files)
    list_of_created_folders = []
    for exts in unique_extensions:
        created_folder = creating_folder("folder.{}".format(exts))
        list_of_created_folders.append(created_folder)
    return list_of_created_folders

print("Creating folders...")
list_of_created_folders = creating_folders_by_extensions(unique_extensions)
print(f"Following folders are created: {list_of_created_folders}")


def sort_file_by_exts(list_of_files, list_of_created_folders):
    for folder in list_of_created_folders:
        replaced_folder = folder.replace(".", " ")
        splitted_folder = replaced_folder.split()
        print(splitted_folder[-1])
        for file in list_of_files:
            replaced_file = file.replace(".", " ")
            splitted_file = replaced_file.split()
            print(splitted_file[-1])
            if splitted_file[-1] == splitted_folder[-1]:
                shutil.move(file, folder)

print("Sorting files...")
sort_file_by_exts(list_of_files, list_of_created_folders)
print("Done.")