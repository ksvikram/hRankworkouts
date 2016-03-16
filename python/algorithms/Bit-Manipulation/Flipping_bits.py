#!/bin/bash
import sys
for _ in range(input()):
    print str(~(input()) +  2**32)


'''
#!/bin/bash
import sys
for _ in range(input()):
    print str(~input() &  0xffffffff)
'''    
