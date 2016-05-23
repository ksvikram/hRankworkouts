import re
R = re.compile(r'http(s)?://(?:(www|ww2).)?([\w\d\.-]+\.[a-zA-Z]+)(?=(/|\?|\"))')

res = set()

for _ in range(input()):
    html = raw_input()
    temp = R.findall(html)
    for i in temp:
        res.add(i[2])
print ';'.join(sorted(res))
