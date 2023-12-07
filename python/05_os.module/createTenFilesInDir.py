#!/usr/bin/env python3

# Description: Function which create 10 files with target content inside target folder.
# input 
# createTenFilesInDir.py folder text


import os
import sys


def creating_files():
    for i in range(10):
        with open("file{}".format(i), "w+") as file:
            file.write(sys.argv[2])
            file.close


os.mkdir(str(sys.argv[1]))
os.chdir(str(sys.argv[1]))
creating_files()