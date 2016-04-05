#!/bin/python
#practice
for _ in range(input()):
    res = False
    n = input()
    a = map(int, raw_input().strip().split(' '))
    
    temp1 = 0
    temp2 = sum(a)
    
    for i in range(n):
        temp2 -= a[i]
        if temp1 == temp2:
            res = True
            break
        temp1 += a[i]    
  
    if res:
        print 'YES'
    else:
        print 'NO'
            
