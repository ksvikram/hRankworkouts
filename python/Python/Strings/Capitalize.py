#!/bin/python
s = raw_input().strip()
s1 = s2 = s.split()
s1 = map(lambda x: x[0].upper() + x[1:]  , s1)
for i in range(len(s2)):
    s = s.replace(s2[i], s1[i])
print s    
