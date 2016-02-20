def isBST(a):
    	stack = []
	lower = -1
	state = True
	for item in a:
		if lower > -1 and item < lower:
			state = False
		while(len(stack) != 0 and stack[len(stack) - 1]  < item ):
			lower = stack.pop()
		stack.append(item)
	
	if state == False:
		print "NO"
	else:
		print "YES"

t = int(raw_input().strip())

for _ in range(t):
    n = int(raw_input().strip())
    l = map(int, raw_input().strip().split())
    isBST(l)
