import sys
import re

x = sys.stdin.read()

R = re.compile(r'((\/\/.*?\n)|(/\*.*?\*/))', re.DOTALL)
res = R.findall(x)

for i in res:
    temp = i[0].strip().split('\n')
    temp = map(lambda x: x.strip(), temp)

    print '\n'.join(temp)
