import re

s = ''
for _ in range(input()):
    s = s + ' ' + raw_input().strip()

for _ in range(input()):
    word = raw_input()
    res = []
    pat = r'(?<=\W)' + re.escape(word) + r'(?=\W)'
    res = re.findall(pat, s)
    print len(res)
