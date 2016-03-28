#!/bin/python
from collections import Counter
for _ in range(input()):
    n = input()
    a = map(int, raw_input().strip().split())
    c = Counter(a)
    temp = map(lambda x : x*(x-1), list(c.values()))
    if len(temp):
        print sum(temp)
    else:
        print '0'
