#!/bin/python
def quickSort(ar):
    l = len(ar)
    if l <= 1:
        return ar
    left, pivot, right = [], ar[0], []
    for i in range(1, l):
        if ar[i] < pivot:
            left.append(ar[i])
        elif ar[i] > pivot:
            right.append(ar[i])   
    left = quickSort(left)        
    right = quickSort(right)
    res = left+[pivot]+right
    print  " ".join(map(str, res))
    return res

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
