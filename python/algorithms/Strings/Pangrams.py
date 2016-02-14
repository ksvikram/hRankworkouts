#!/bin/python
s = raw_input().strip()
s = set(s.replace(' ', '').lower())
if len(s) == 26:
    print 'pangram'
else:
    print 'not pangram'
