#!/bin/python
import re

for _ in range(input()):
    n = raw_input().strip()
    if n.isalnum() and len(n) == 10 and len(set(n)) == len(n) and len(re.findall(r'[A-Z]', n)) >= 2 and len(re.findall(r'[0-9]', n)) >= 3:
                    print 'Valid'
    else:
        print "Invalid"
