#!/usr/bin/python
def lonelyinteger(a):
    answer = 0
    answer = reduce(lambda x, y: x ^ y, a)
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
