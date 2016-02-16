from collections import *    
a=Counter(raw_input())
b=Counter(raw_input())
c=a-b;d=b-a;e=c+d
print len(list(e.elements()))

'''
#slower 
s1 = raw_input().strip()
s2 = raw_input().strip()

if len(s1) > len(s2):
    s1, s2 = s2, s1
for i in s1:
    if i in s2:
        l1 = list(s1)
        l2 = list(s2)
        del(l1[s1.find(i)])
        del(l2[s2.find(i)])
        s1 = ''.join(l1)
        s2 = ''.join(l2)
  
print len(s1) + len(s2)


'''
