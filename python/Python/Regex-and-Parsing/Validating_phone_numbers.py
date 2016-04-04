#!/bin/python
import re

for _ in range(input()):
    n = raw_input().strip()
    if n.isdigit() and len(n) == 10 and bool(re.match(r'^[7-9]\d+', n)):
        print 'YES'
    else:
        print 'NO'
