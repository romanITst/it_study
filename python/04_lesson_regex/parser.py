#!/usr/bin/env python3

# Description: This script uses for parsing nginx logs


import sys
import re


def line_report(line): 
    """
    Returns from the logs file line IP address,
    bytes sent, status, request time and agent
    """
    splitted_line = line.split()
    return { "IP address": splitted_line[0],
            "Bytes sent": splitted_line[9],
           # "Status": splitted_line[8],
           # "Request time": splitted_line[3],
           # "Agent": splitted_line[11]
    }


def log_report(logfile):
    report = {}
    #sum_of_bytes_sent = 0
    sum_of_bytes_sent = []
    for line in logfile:
        line_dict = line_report(line)
        ip_address = line_dict["IP address"]
        bytes_sent = int(line_dict["Bytes sent"])
        #status = line_dict["Status"]
        #request_time = line_dict["Request time"]
        #agent = line_dict["Agent"]
        #sum_of_bytes_sent += int(bytes_sent)
        sum_of_bytes_sent.append(bytes_sent)
        sum2 = sum(sum_of_bytes_sent)
        print(sum2)
        report.setdefault(ip_address, []).append(bytes_sent)
    return report


with open("access.log", "r") as log:
    result = log_report(log)
    print(result)