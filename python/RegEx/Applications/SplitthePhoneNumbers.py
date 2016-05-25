import re

R = re.compile(r'(\d{1,3})[\-\ ](\d{1,3})[\-\ ](\d{4,10})')

for _ in range(input()):
    line = raw_input()
    match = R.search(line)
    if match:
        print 'CountryCode={},LocalAreaCode={},Number={}'.format(match.group(1), match.group(2), match.group(3))
