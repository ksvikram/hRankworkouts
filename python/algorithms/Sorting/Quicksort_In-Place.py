#!/bin/python
def partition(ar, low, high):
    pivot = ar[high]
    i = low
    for j in range(low, high):
        if ar[j] <= pivot:
            ar[i], ar[j] = ar[j], ar[i]
            i += 1
    ar[i], ar[high] = ar[high], ar[i]
    print ' '.join(map(str, ar))
    return i

def quickSort(ar, low, high):
    if low < high:
        p = partition(ar, low, high)
        quickSort(ar, low, p-1)
        quickSort(ar, p+1, high)

        
        
m = input()
ar = [int(i) for i in raw_input().strip().split()]
low = 0
high = len(ar)
quickSort(ar, low, high-1)
