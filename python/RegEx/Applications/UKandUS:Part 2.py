import re

pat = re.compile('our')

s = ''
for _ in range(input()):
    s += raw_input() + ' '

s = pat.sub('or', s)

for _ in range(input()):
    w = raw_input()
    w = pat.sub('or', w)
    res = re.findall(r'\b' + re.escape(w) + r'\b', s)
    print len(res)
