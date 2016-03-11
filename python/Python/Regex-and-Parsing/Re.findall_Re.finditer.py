#!/bin/python
import re
consonants = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
vowels = "AEIOUaeiou"

s = raw_input().strip()
res = re.findall(r'(?=([%s][%s]{2,}[%s]))' %(consonants,vowels,consonants), s) # extract vowels occuring in b/n consonants with lookahaead
r = re.findall(r'[aeiouAEIOU]+', ''.join(res)) # extract vowels occuring in b/n consonants
print("\n".join(r) if r else -1) 
