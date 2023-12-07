#!/usr/bin/env python3

# Description: This script creates a target folder(if it does not exist),
# and 10 folders in it, and 10 folders in each of this and 10 files in last folders. 
# input:                                                        
# folder_generator.py [1] [2] [3] [4]
# [1] - main_folder / [2] - subfolder_1_lvl / [3] - subfolder_2_lvl                   
# [4] - files
# folder_generator.py music artist album song
# output: music
#         ├── artist00
#         │   ├── album00
#         │       ├── song00
#         │       ...   
#         │       └──song09
#         │   └── album09
#         ├── artist01
#         ...


import os
import sys


def creating_folder(folder_name):
    '''
    This function creates folder
    with necessary name or path
    and returns its name/path
    '''
    created_folder = os.mkdir(folder_name)
    return created_folder


def creating_file(file_name):
    '''
    This function creates folder
    with necessary name or path
    and returns its name/path
    '''
    with open(file_name, "w+") as created_file:
        created_file.close()
    return created_file


def creating_subfolders():
    for i in range(10):
        lvl_1_folder = str(sys.argv[2] + "0{}".format(i))
        creating_folder(lvl_1_folder)
        os.chdir(lvl_1_folder)
        for s in range(10):
            lvl_2_folder = str(sys.argv[3] + "0{}".format(s))
            creating_folder(lvl_2_folder)
            os.chdir(lvl_2_folder)
            for g in range(10):
                file_name = str(sys.argv[4] + "0{}".format(g))
                creating_file(file_name)
            os.chdir("..")
        os.chdir("..")

if os.path.exists(str(sys.argv[1])):
    try:
        creating_folder(str(sys.argv[1]))
    except: FileExistsError
    print("Directory you entered is already exists. Continue?")
    if str(input("[yes/no]: ")) == "yes":
        os.chdir(str(sys.argv[1]))
        print("Creating subfolders and files...")
        creating_subfolders()
        print("Done.")
        sys.exit(1)
    else:
        print("You chose 'no'. Exit.")
        sys.exit(1)

if not os.path.exists(str(sys.argv[1])):
    print("Directory you entered doesn't exists. Create it?")
    if str(input("[yes/no]: ")) == "yes":
        print("Creating target folder...")
        creating_folder(str(sys.argv[1]))
        os.chdir(str(sys.argv[1]))
        print("Creating subfolders and files...")
        creating_subfolders()
        print("Done.")
        sys.exit(1)
    else:
        print("You chose 'no'. Exit.")
        sys.exit(1)