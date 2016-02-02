#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
res = 0
for i in range(n):
    res = res - (a[i][i] - a[i][n - i - 1])
   
print abs(res)    
