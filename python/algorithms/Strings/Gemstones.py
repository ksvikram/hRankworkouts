#!/bin/python

n = int(raw_input().strip())
res = set()
for i in range(n):
    s = set(raw_input().strip())
    if res:
        res = res & s
    else:
        if i == 0:
            res = s
        else:
            break
            
print len(res)    
    
