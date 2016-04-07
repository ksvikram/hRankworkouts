#!/bin/python
import re
S = raw_input().strip()
k = raw_input().strip()
ls,lk = len(S),len(k)

noneFound = True

for i in xrange(ls-lk+1):
    if k==S[i:i+lk]:
        print (i,i+lk-1)
        noneFound = False
        
if noneFound: print (-1,-1)


'''
# editorial
import re
S = raw_input()
k = raw_input()
anymatch = 'No'
for m in re.finditer(r'(?=('+k+'))',S):
    anymatch = 'Yes'
    print (m.start(1),m.end(1)-1)
if anymatch == 'No':
    print (-1, -1)
    
  '''
    
