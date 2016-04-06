#!/bin/python
#practice
#faster method
for _ in range(input()):
    m = input()
    n = input()
    a = map(int, raw_input().strip().split())
 
    for i in range(n):
        if a[i] < m:
            temp = m - a[i]
            if temp in a[i+1:]:
                print i+1, a[i+1:].index(temp)+(i+1)+1
                break

'''
#!/bin/python
# normal naive method
for _ in range(input()):
    m = input()
    n = input()
    a = map(int, raw_input().strip().split())
    for i in range(n):
        if a[i] < m:
            temp = m - a[i]
            for j in range(i,n):
                if j != i and a[i]+a[j] == m:
                    print i+1, j+1
                    break
'''
