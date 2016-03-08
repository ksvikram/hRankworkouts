#!/bin/python
for _ in range(input()):
    s = raw_input().strip()
    res = 0
    rev = s[::-1]
    for i in range(len(s)/2):
        res += abs(ord(s[i]) - ord(rev[i]))
    print res    
