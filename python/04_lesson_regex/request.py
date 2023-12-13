#!/usr/bin/env python3

# This script is sending requests to the site you need

import requests


for r in range(10):
    res = requests.get("http://localhost")
print(res)