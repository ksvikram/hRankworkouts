#!/bin/python
import re

p = raw_input().strip()
res = bool(re.match(r'^[1-9][\d]{5}$', p)) and (len(re.findall(r'(?=(\d)\d\1)', p)) <= 1)
print res
