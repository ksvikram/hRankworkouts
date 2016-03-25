#!/bin/python
#practice
n, k , q = raw_input().split()
n, k, q = int(n), int(k), int(q)
a = map(int, raw_input().strip().split())
l = len(a)
rem = k%l
for i in range(q):
    x = input()
    print a[(x-rem)%l ]
