import re

s = ''
for i in range(input()):
    s = s + ' ' + raw_input().strip()

for i in range(input()):
    substr = raw_input()
    pat =  r'\w+' + re.escape(substr) + r'\w+'
    res = re.findall(pat, s)
    print len(res)   
    
