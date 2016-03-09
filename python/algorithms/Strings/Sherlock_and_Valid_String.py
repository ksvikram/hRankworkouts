#!/bin/bash
from collections import Counter
s = raw_input().strip()
c = Counter(s)
x = c.values()[0]
count = 0
for i in c.values():
    if x != i:
        count += 1       
if count > 1:
    print "NO"
else:
    print "YES"
