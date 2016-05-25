import re

R = re.compile(r'^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}')

for _ in range(input()):
    if R.match(raw_input()):
        print 'VALID'
    else:
        print 'INVALID'
