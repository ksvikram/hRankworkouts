import re

R  = re.compile(r'hackerrank', re.IGNORECASE)

count = 0
for _ in range(input()):
    count += len(R.findall(raw_input()))
    
print count    
    
