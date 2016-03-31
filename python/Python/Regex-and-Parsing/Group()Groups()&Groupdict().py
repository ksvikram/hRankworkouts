#!/bin/python
import re
n = raw_input()
m = re.search(r'([A-Za-z0-9])\1', n)
print(m.group(1) if m else -1)
