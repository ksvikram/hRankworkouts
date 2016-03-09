#!/bin/python
for _ in (range(int(input()))):
    s1 = raw_input().strip() + "z"
    s2 = raw_input().strip() + "z"
    res = ''
    j = k =  0
    while (j < len(s1)) and (k < len(s2)):
        if s1[j:] < s2[k:]:
            res += s1[j]
            j += 1
        else:
            res += s2[k]
            k += 1
    res += s1[j:]
    res += s2[k:]
 
    print res[:-2]
