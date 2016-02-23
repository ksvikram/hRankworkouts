#!/bin/python

s = list(raw_input().strip())
s = ''.join(map(lambda x: x.upper() if x.islower() else x.lower(), s))
print s

'''
#another method
import string
print string.swapcase(raw_input())
'''
