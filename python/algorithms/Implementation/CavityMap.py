#!/bin/python
n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
   grid_t = str(raw_input().strip())
   grid.append(grid_t)
i = 0
for arr in grid:
    if i == 0 or i == n-1:
        print arr.strip()
    else:
        for j in range(1, n-1):
            if arr[j] > arr [j-1] and arr[j] > arr[j+1] and arr[j] > grid[i-1][j] and arr[j] > grid[i+1][j]:
                arr = arr[:j] + 'X' + arr[j+1:]
         
        print arr.strip()
    i +=1       
