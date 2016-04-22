#!/bin/python
#practice
import re

for _ in range(int(input())):
    card = raw_input().strip()
    print('Valid' if re.search(r'^[456]\d{3}(-?)(\d{4}\1){2}\d{4}$', card) and not re.search(r'(\d)(\1{3}|(\1|-){4})', card) else 'Invalid')
