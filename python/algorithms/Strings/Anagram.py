#!/bin/python
from collections import Counter

t = int(raw_input().strip())

for _ in range(t):
    s = raw_input().strip()
    if len(s)%2 != 0:
        print '-1'
    else:
        pvt = len(s)/2
        s1 = s[:pvt]
        s2 = s[pvt:]
        c1 = Counter(s1)
        c2 = Counter(s2)
        print sum((c2 - c1).values())
