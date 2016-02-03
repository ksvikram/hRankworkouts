#!/bin/python
''' My version _ Some tests fails, but they pass if run individually'''
import re

time = raw_input().strip()
is_pm = False
if re.search(r'(PM)$', time, re.M|re.L):
    is_pm = True

time = re.sub(r'((A|P)M)', '', time)    
temp_arr = list(time.split(':'))

if is_pm == True and int(temp_arr[0]) < 12:
  temp_arr[0] = str(int(temp_arr[0]) + 12)

if is_pm == False and int(temp_arr[0]) == 12:
    temp_arr[0] = '00'

    time = ':'.join(temp_arr)
print time
'''


#!/bin/python
import re

ins = raw_input().strip()

is_pm = ins[-2:].lower() == 'pm'
time_list = list(map(int, ins[:-2].split(':')))

if is_pm and time_list[0] < 12:
    time_list[0] += 12

if not is_pm and time_list[0] == 12:
    time_list[0] = 0

print(':'.join(map(lambda x: str(x).rjust(2, '0'), time_list)))
