#!/bin/python
#practice
n = input()
a = map(int, raw_input().strip().split())

sorted_array = sorted(a)
if a == sorted_array:
    print 'yes'
else:
    temp_array = []
   
    for i, (x, y) in enumerate(zip(a, sorted_array)):
        if x != y:
            temp_array.append(i)
        if len(temp_array) > 2:
            break
    if len(temp_array) == 2:
        print 'yes'
        print 'swap', temp_array[0]+1, temp_array[1]+1
    else:
        index = sorted_array.index(a[temp_array[0]])+1 
        temp = a[temp_array[0]:index][::-1]
        if temp == sorted_array[temp_array[0]:index]:
            print 'yes'
            print 'reverse', temp_array[0]+1, index
        else:
            print 'no'
