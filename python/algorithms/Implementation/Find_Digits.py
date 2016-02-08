#!/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    n = raw_input().strip()
    arr = map(int, list(n))
    n = int(n)
    count = 0
    count = map(lambda x: count + 1 if x != 0 and n%x == 0 else 0, arr)
    print sum(count)
