def mygcd(a, b):
	while b:
		a , b = b, a%b
	return abs(a)


t = int(raw_input().strip())

for _ in range(t):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split())
    if reduce(mygcd, a) > 1:
        print "NO"
    else:
        print "YES"
