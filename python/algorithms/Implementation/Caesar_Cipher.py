#!/bin/python
n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

if k > 26:
    k %=26

def enc(x):
    if x.isupper() :
         x = ord(x) + k
         if x > 90:
            x -= 26
    elif x.islower():
         x = ord(x) + k
         if x > 122:
            x -= 26        
    return chr(x)            
    
char_list = list(s)
new_list = ''.join(map(lambda x: enc(x) if x.isalpha() else x, s))
print new_list

