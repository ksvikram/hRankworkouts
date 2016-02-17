#!/bin/python
t = int (raw_input().strip())

for _ in range(t):
    s1 = set(raw_input().strip())
    s2 = set(raw_input().strip())
    if s1.intersection(s2):
        print "YES"
    else:
        print "NO"
