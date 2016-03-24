#!/bin/python
#practice
n = int(input())
assert 1 <=n <= 1000000
freq = [0] * 100

for i in xrange(n):
    arr = raw_input().split()
    number = int(arr[0])
    freq[number] = freq[number] + 1

x = 0
for i in xrange(100):
    x = x + freq[i]
    print x,
