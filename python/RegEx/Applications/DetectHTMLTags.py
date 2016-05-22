import re

pattern = r'<\s*([a-z]+\d?)\s*>?'
res = set()
for _ in range(input()):
    html = raw_input()
    res |= set(re.findall(pattern, html))
    
print ';'.join(sorted(res))    
