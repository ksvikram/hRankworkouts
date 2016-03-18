#!/bin/python
#practice
for _ in range(input()):
    res = 0
    n = input()
    ar = map(int, raw_input().strip().split())
    # if array is of odd length, xor all items in odd position
    if len(ar)%2 != 0 :
        for i in range(0, len(ar)+1/2,2):
            res ^= ar[i]
    print res    
