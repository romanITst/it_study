#!/usr/bin/env python3

# Description: This script creates a target folder(if it does not exist),
# and 10 folders in it, and 10 folders in each of this. Example: 
# pass


import os
import sys


def creating_folder(folder_name):
    '''
    This function is creates folder
    with necessary name or path
    and returns its name/path
    '''
    created_folder = os.mkdir(folder_name)
    return created_folder

creating_folder(str(sys.argv[1]))
os.chdir(str(sys.argv[1]))

for i in range(int(sys.argv[3])):
    lvl_1_folder = str(sys.argv[2] + "0{}".format(i))
    creating_folder(lvl_1_folder)
    os.chdir(lvl_1_folder)
    for s in range(int(sys.argv[5])):
        lvl_2_folder = str(sys.argv[4] + "0{}".format(s))
        creating_folder(lvl_2_folder)
    os.chdir("..")