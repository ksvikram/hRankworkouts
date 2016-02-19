from collections import Counter
found = False
string = raw_input()
length = len(string)
string = Counter(string)
if length%2 == 0:
    if sum(string.values())%2 == 0:
        found = True
    else:
        found = False
else:
    if len(filter(lambda x: x%2 != 0, string.values())) == 1:
        found  = True
    else:
        found = False

if not found:
    print("NO")
else:
    print("YES")
