import re
s = ''
for _ in range(input()):
    s += raw_input() + ' '

for _ in range(input()):
    w = raw_input()
    pat = (re.escape(w[:-2]) + r'(ze|se)')
    res = re.findall(pat, s)
    print len(res)
