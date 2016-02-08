import math

t = int(raw_input().strip())
for a0 in xrange(t):
    n1, n2 = map(int, raw_input().strip().split(' '))
    if ( 1<= n1 and n1<=n2 and n2 <= math.pow(10, 9)):
        l = int(math.ceil(math.sqrt(n1)))
        h = int(math.floor(math.sqrt(n2)))
        print h - l + 1
    else:
        print 0
