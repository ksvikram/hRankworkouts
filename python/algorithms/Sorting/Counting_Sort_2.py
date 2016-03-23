#!/bin/python

n = input()
x = map(int, raw_input().strip().split())
assert 0 <= len(x) <= n

freq = [0] * 100
j = 0
for i in x:
    freq[i] = freq[i] + 1

for index in xrange(n):
    for i in xrange(freq[index]):
        print index, 
