#!/bin/python
import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
 
    n1 = n
    while(n1%3 != 0):
        n1 -= 5
   
    if n1 < 0:
        print -1
    else:
        print '5'* n1 + '3'*(n-n1)
