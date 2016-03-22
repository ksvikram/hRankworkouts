#!/bin/python

swaps = 0
shifts = 0
def insertionSort(ar):
    global shifts
    for i in range(1, len(ar)):
        key = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > key:
            ar[j+1] = ar[j]
            shifts += 1
            j -= 1
        ar[j+1] = key
    
def partition(ar, low, high):
    global swaps
    pivot = ar[high]
    i = low
    for j in range(low, high):
        if ar[j] <= pivot:
            ar[i], ar[j] = ar[j], ar[i]
            i += 1
            swaps += 1
    ar[i], ar[high] = ar[high], ar[i]
    swaps += 1
    return i
    
def quickSort(ar, low, high):
    global swaps
    if low < high:
        p = partition(ar, low, high)
        quickSort(ar, low, p - 1)
        quickSort(ar, p+1, high)

    
n = input()
x = map(int, raw_input().strip().split())

assert -1000 <= len(x) <= 1000
low = 0
high = len(x)
insertionSort(x[:])
quickSort(x[:], low, high-1)
print shifts - swaps
    
