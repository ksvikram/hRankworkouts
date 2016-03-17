#!/bin/python
for _ in range(input()):
    n = input()
    l = 1
    while n!= 1:
        if (n & (n-1)) == 0:
            n = n/2
        else:
            x = 1
            while x < n:
                x <<= 1
            n -= x >> 1
        l = ~l
    if l != 1:
        print "Louise"
    else:
        print "Richard"

'''
#!/bin/python
import math

for _ in range(input()):
    n = input()
    l = 0
    while n!= 1:
        x = 2**int(math.log(n, 2))
        if n == x:
            n = n/2
        else:
            n -= x
        l = 1 - l
    if l :
        print "Louise"
    else:
        print "Richard"
        

'''
