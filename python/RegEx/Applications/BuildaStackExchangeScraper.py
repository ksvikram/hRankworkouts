import re
import sys

R1 = re.compile(r'\<h3\>\<a href="\/questions\/(\d+)\/.*?\>(.*?)\<.*?class\=\"relativetime\"\>(.*?)\<', re.S)

x = sys.stdin.read()
res = R1.findall(x)
for item in res:
    print ';'.join(list(item))
