#!/usr/bin/env python3

# Description: This script is parsing logs


import sys


def splitting_line(line):
    splitted_line = line.split()
    return splitted_line


# line = r'127.0.0.1 - - [28/Nov/2023:17:08:07 +0300] "GET / HTTP/1.1" 200 396 "-" "python-requests/2.25.1"'
# splitted_line = line.split()
# ipaddr = line[3]
# print(splitted_line)
# print(ipaddr)