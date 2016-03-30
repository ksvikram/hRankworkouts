#!/bin/python
import re
for _ in range(input()):
    n = raw_input().strip()
    print bool(re.match(r'^[\+\-]?\d*\.\d+$', n))
