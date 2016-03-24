#!/bin/python
#practice
n = input()
assert 2 <= n <= 200000
a = list(map(int, raw_input().split()))
a.sort()
x = []
res = 10**7

for i in range(len(a) -1):
    new_res = a[i+1] - a[i]
    if new_res < res:
        x = [a[i], a[i+1]]
        res = new_res
    elif new_res == res:
        x.append(a[i])
        x.append(a[i+1])
print ' '.join(map(str, x))
