import re

R = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]$')

for _ in range(input()):
    if R.match(raw_input()):
        print 'YES'
    else:
        print 'NO'
