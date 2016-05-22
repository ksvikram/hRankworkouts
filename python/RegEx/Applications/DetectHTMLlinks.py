import re

pat = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'

N = int(raw_input())
for _ in range(N):
    html = raw_input()
    res = re.findall(pat, html)
    print res
    for link, title in res:
        print "{},{}".format(link, title.strip())
