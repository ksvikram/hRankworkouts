#!/bin/python

a = set(raw_input().strip().split())
n = int(raw_input().strip())
res = 'True'
for i in range(n):
    s = set(raw_input().strip().split())
    if len(a.intersection(s)) != len(s) or len(s) == len(a):
        res = 'False'
        break
print res        
