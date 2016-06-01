import re
import sys

x = sys.stdin.read()

if re.search('#include', x):
    print 'C'
elif re.search('import java', x):
    print 'Java'
else:
    print 'Python'
