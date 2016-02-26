#!/bin/python
happiness = 0
n , m = (raw_input().strip().split())
arr = raw_input().strip().split()

A = set(raw_input().strip().split())
B = set(raw_input().strip().split())

for i in arr:
    if i in A:
        happiness +=1
    if i in B:
        happiness -=1
print happiness        
