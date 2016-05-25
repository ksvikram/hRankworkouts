import re

R = re.compile(r'[Hh][Ii]\ (?![Dd]).*?')

for _ in range(input()):
    line = raw_input()
    match = R.match(line)
    if match:
        print line
