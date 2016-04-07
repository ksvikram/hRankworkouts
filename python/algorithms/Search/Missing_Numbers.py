#!/bin/python
from collections import Counter

n = input()
a1 = raw_input().strip().split()
m = input()
a2 = raw_input().strip().split()

c1 = Counter(a1)
c2 = Counter(a2)
res = set((c2-c1).elements()) #should not use list here. or else duplicates will show up
print ' '.join(sorted(res))
