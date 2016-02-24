#!/bin/python
st = str(raw_input().strip())
l = len(st)
k = s = 0
for i in range(l):
    if st[i] in ['A','E', 'I', 'O', 'U']:
        k += l - i
    else: 
        s += l - i
if k > s:
    print 'Kevin', k
elif s > k:
    print 'Stuart', s
else:
    print 'Draw'
