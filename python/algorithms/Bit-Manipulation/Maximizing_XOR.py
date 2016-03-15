#!/bin/python
# my solution
def  maxXor( l,  r):
    max = -1
    for i in range(l, r+1):
        for j in range(i, r+1):
            if (i ^ j) > max:
                max = (i ^ j)
    return max            

_l = int(raw_input());
_r = int(raw_input());
res = maxXor(_l, _r);
print(res)

'''
#better solution
def maxXOR(L,R):
    P = L^R
    ret = 1
    while(P): # this one takes (m+1) = O(logR) steps
        ret <<= 1
        P >>= 1
    return (ret - 1)

print(maxXOR(int(input()),int(input())))
'''
