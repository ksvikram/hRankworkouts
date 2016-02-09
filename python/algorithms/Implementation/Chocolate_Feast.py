#!/bin/python
t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    chocs = n/c
    wraps = chocs
    while wraps >= m:
        chocs = chocs + wraps/m
        rem = wraps%m
        wraps = wraps/m + rem
    print chocs
