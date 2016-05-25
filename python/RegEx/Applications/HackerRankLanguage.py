import re

ar = ['C', 'CPP', 'JAVA', 'PYTHON', 'PERL', 'PHP', 'RUBY', 'CSHARP', 'HASKELL', 'CLOJURE', 'BASH', 'SCALA', 'ERLANG', 'CLISP', 'LUA', 'BRAINFUCK', 'JAVASCRIPT', 'GO', 'D','OCAML', 'R', 'PASCAL', 'SBCL', 'DART', 'GROOVY', 'OBJECTIVEC']

R = re.compile(r'\b([A-Z]+)\b', re.IGNORECASE)

for _ in range(input()):
    line = raw_input()
    match = R.search(line)
    if match.group(0) in ar:
        print 'VALID'
    else:
        print 'INVALID'
