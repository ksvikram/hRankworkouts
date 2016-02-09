#!/bin/python
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
while(len(arr)):
    minimum = min(arr)
    print len(arr)
    arr = map(lambda x: x - minimum, arr)
    arr = filter(lambda x: x > 0, arr)
