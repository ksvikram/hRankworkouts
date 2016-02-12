#!/bin/python
d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

daily_fine = 15
monthly_fine = 500
year_fine = 10000

if y1 < y2:
    print 0
elif y1 > y2:    
    print year_fine
else:
    if m1 < m2:
        print 0
    elif m1 > m2:
        print (m1- m2) * monthly_fine
    elif d1 <= d2:
        print 0
    else:       
        print (d1- d2) * daily_fine
