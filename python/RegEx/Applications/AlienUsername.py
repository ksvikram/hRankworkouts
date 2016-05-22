import re
for _ in range(input()):
    uname = raw_input()
    pat = r'^[_\.]\d+[a-zA-Z]{0,}(_)?$'
    
    if bool(re.match(pat, uname)):
        print "VALID"
    else:
        print "INVALID"
