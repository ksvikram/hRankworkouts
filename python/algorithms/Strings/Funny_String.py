#!/bin/python
t = int(raw_input().strip())
for _ in range(t):
    s = list(raw_input().strip())
    str_len = len(s)
    status = False
    for j in range(1, str_len-1):
        a = abs(ord(s[j]) - ord(s[j-1]))
        b = abs(ord(s[str_len-j]) - ord(s[str_len - j -1]))
        if a == b:
            status = True
        else:
            status = False
            break
    if status == True:
        print 'Funny'
    else:
        print  'Not Funny'
