#!/usr/bin/env python3

# Description: This script uses for parsing nginx logs


import sys

logfile = open("access.log", "r")
line = logfile.readline()
# with open("access.log") as logs_file:
#     for line in logs_file:
#         line = asd


def splitting_line(line):
    """
    Return splitted line
    """
    splitted_line = line.split()
    return splitted_line

splitted_line = splitting_line(line)


def line_report(splitted_line): 
    """
    Return IP address and bytes sent
    """
    ipaddress = splitted_line[0]
    bytes_sent = splitted_line[9]
    logline = {f"IP address": ipaddress, "Bytes sent": bytes_sent}
    return logline


for line in logfile:
    line = line_report(splitted_line)
    print(line)