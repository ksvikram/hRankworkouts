#!/bin/python
#practice
def insertionSort(ar):
    e = ar[-1]
    l = len(ar)
    i = l - 2
    for j in range(i, -2, -1 ):
        if j == -1:
            ar[j+1] = e
            a = ' '.join(map(str, ar))    
            print a    
            break
        if e < ar[j]:
            ar[j+1] = ar[j]
            a = ' '.join(map(str, ar))    
            print a            
        else:
            ar[j+1] = e
            a = ' '.join(map(str, ar))    
            print a            
            break
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
