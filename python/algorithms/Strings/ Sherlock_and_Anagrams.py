from collections import defaultdict

for _ in range(int(raw_input())):
    s = raw_input().strip()
    d = defaultdict(int)
    l = len(s)
    res = 0
    for i in range(l):
        for j in range(i, l):
            w = ''.join(sorted(s[i:j+1]))
            res += d[w]
            d[w] += 1
    print res
