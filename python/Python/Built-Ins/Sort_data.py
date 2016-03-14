#!/bin/python

n, m = (raw_input().strip().split())
n, m = (int(n), int(m))
t = [ map(int, raw_input().strip().split())  for i in range(n) ]
k = input()
t.sort(key = lambda x:x[k])

for i in range(n):
    print " ".join(map(str, t[i]))
