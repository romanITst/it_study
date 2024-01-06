#!/usr/bin/env python3

# Description: This script shows a few examples of reg. expressions
# by re.search(), re.findall(), re.match():


import re

# Example 1: Matching email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
text = "Contact roman@gmail.com for assistance or visit www.example.com."
emails = re.findall(email_pattern, text)
print(emails)  # Output: ['roman@example.com']

# Example 2: Extracting dates in MM/DD/YYYY format
date_pattern2 = r'\b\d{1,2}/\d{1,2}/\d{4}\b'
text2 = "Meeting on 05/20/2023 is rescheduled to 06/10/2023."
dates2 = re.findall(date_pattern2, text2)
print(dates2)   # Output: ['05/20/2023', '06/10/2023']


# with re.compile():

pattern3 = re.compile(r'\b\d{1,2}/\d{1,2}/\d{4}\b')
text3 = "Meeting on 17/11/2023 is rescheduled to 19/12/2023."
dates3 = pattern3.findall(text3)
print(dates3)   # Output: ['17/11/20233', '19/12/2023']