s = raw_input().strip()
s1 = raw_input().strip()

count = 0
for i in range(len(s)):
     index = s.find(s1)
     if index != -1:
        count += 1
        s = s[index+1:]
print count        
