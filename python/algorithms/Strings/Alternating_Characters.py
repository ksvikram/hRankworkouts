#!/bin/python

t = int(raw_input().strip())

for _ in range(t):
    delete = 0
    s = list(raw_input().strip())
    for i in range(0, len(s)- 1):
        if s[i] == s[i+1]:
            delete += 1
    print delete            
