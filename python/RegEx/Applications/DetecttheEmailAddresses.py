import re

pat = r'([\w]+[\w\d\.]+\@([a-zA-Z0-9]+\.)+[a-zA-Z]{2,3})'
res = set()

for _ in range(input()):
    line = raw_input()
    temp = re.findall(pat, line)

    for i in temp:
        res.add(i[0])
print ';'.join(sorted(res))
