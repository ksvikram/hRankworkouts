import re

R1 = re.compile(r'^(?=hackerrank).*?(?<=hackerrank)$')
R2 = re.compile(r'^hackerrank.*?(?<!hackerrank)$')
R3 = re.compile(r'^(?!hackerrank).*?(hackerrank)$')

for _ in range(input()):
    line = raw_input().strip()
    if R1.search(line):
        print '0'
    elif R2.search(line):
        print '1'
    elif R3.search(line):
        print '2'
    else:
        print '-1'
