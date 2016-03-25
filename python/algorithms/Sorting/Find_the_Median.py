#!/bin/python
n = input()
assert 1 <=n <= 1000001
assert n%2
ar = map(int, raw_input().strip().split())
ar.sort()
print ar[len(ar)/2]
    
