#!/bin/python
t = int(raw_input().strip())
for i in range(t):
    n = int(raw_input().strip())
    a = int(raw_input().strip())
    b = int(raw_input().strip())
 
    diff = max(a, b) - min(a,b)
    first_res = min(a, b) * (n-1)

    res = []
    cur_no = first_res
    if a == b:
        res.append(first_res)
    else:        
        for i in range(n):
            res.append(cur_no)
            cur_no = cur_no + diff
    res = map(str, res)        
    print ' '.join(res)
