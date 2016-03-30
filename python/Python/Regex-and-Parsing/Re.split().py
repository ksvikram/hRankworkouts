#!/bin/python
import re

res = re.split(r'[\,\.]', raw_input().strip())
for i in res:
    if i.isdigit():
        print i
