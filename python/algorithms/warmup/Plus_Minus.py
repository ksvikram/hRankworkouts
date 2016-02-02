#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

print format(float(len(filter(lambda x: x > 0, arr)))/len(arr), '.6f')
print format(float(len(filter(lambda x: x < 0, arr)))/len(arr), '.6f')
print format(float(len(filter(lambda x: x == 0, arr)))/len(arr), '.6f')
