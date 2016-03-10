#!/bin/python
import re
n = input()

for _ in range(n):
    s = raw_input().strip()
    if len(filter( lambda x:  x.isdigit() and 1 < int(x) < 256,  s.split('.'))) == 4:
        print "IPv4"
    elif len(filter( lambda x:  x.isalnum() and not re.search(r'[g-zG-Z]', x),  s.split(':'))) == 8:
        print 'IPv6'
    else:
        print 'Neither'
