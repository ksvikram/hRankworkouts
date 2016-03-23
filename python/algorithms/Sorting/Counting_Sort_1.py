#!/bin/python
#from collections import defaultdict 

n = input()
x = list(map(int, raw_input().strip().split()))
freq = [0]*100
for i in x:
    freq[i] = freq[i]+1
print " ".join(map(str, freq))
