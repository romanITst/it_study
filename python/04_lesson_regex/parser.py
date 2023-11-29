#!/usr/bin/env python3

# Description: This script is parsing logs


import sys

line = r'127.0.0.1 - - [28/Nov/2023:17:08:07 +0300] "GET / HTTP/1.1" 200 396 "-" "python-requests/2.25.1"'
def splitting_line(line):
    """Return splitted line"""
    splitted_line = line.split()
    return splitted_line

splitted_line = splitting_line(line)


def line_report(splitted_line): 
    ipaddres = splitted_line[0]
    bytes_sent = splitted_line[9]
    logline = {f"IPaddres": ipaddres, "Bytes sent": bytes_sent}
    return logline

logline = line_report(splitted_line)
print(logline)

