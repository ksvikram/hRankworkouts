#!/bin/python
import email.utils
import re

n = input()

for _ in range(n):
    (name, address) = email.utils.parseaddr(raw_input().strip())
    if (bool(re.match(r'[A-Za-z][A-Za-z0-9\-\.\_]+@[A-Za-z]+.([A-Za-z]{1,3}$)', address))):
        print name, '<'+address+'>'

'''
import re
from email.utils import *
lst = list()
for i in range(int(raw_input())):
    email = parseaddr(raw_input())
    if bool(re.search(r'^[\w\d\-\.]+@[A-Za-z0-9]+\.\w{1,3}$',email[1])):
        print formataddr(email)
'''
