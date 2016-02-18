t = int(input())

for testCase in range(t):
    testString = raw_input().strip()
    reverseString = testString[::-1]
    if testString == reverseString:
        print(-1)
        continue
    for i in range(len(testString)):
        if testString[i] != reverseString[i]:
            removed = testString[:i] + testString[i+1:]
            if removed == removed[::-1]:
                print(i)
            else:
                print(len(testString)-i-1)
            break
