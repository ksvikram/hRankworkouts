#!/bin/python
n = int(raw_input().strip())
h = map(int, raw_input().strip().split())

print float(sum(set(h)))/len(set(h))
