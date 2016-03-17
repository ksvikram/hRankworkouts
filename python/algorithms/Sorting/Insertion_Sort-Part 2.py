#!/bin/python
def insertionSort(ar):
    l = len(ar)
    for i in range(1, l):
        key = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > key:
            ar[j+1] = ar[j]
            j -= 1
        ar[j+1] = key
        print " ".join(map(str, ar))
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
