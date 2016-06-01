import re
from collections import defaultdict

tag = re.compile(r'(<([a-zA-Z0-9]+).*?>)')
att = re.compile(r'( ([a-zA-Z0-9]+)\=(.*?) ?)')
d = defaultdict(set)

for _ in range(input()):
    string = raw_input()
    res = tag.findall(string)
    for item in res:
        res1 = att.findall(item[0])
        item2 = ''
        if res1:
            for item2 in res1:
                d[item[1]].add(item2[1])
        else:
            d[item[1]].add(item2)
    
for key in sorted(d.keys()):
    print '{}:{}'.format(key, ','.join(sorted(d[key])))
