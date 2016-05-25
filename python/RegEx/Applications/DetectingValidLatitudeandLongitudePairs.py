import re

R = re.compile(r'\(([\+\-]?[\d]{1,2}(\.[\d]+)?)\, ([\+\-]?[\d]{1,3}(\.?[\d]+)?)\)')

for _ in range(input()):
    s = raw_input()
    res = R.search(s)
   
    if (res):
        if  (-90 <= float(res.group(1)) <= 90) and (-180 <= float(res.group(3)) <= 180):
            print 'Valid'
        else:
            print 'Invalid'
    else:
        print 'Invalid'
