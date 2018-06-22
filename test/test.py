import os,sys
import re
path = 'P:\RESEARCH\SQL Jobs\GPA Calculation\STEP1_STUDENT_ACAD_CRED.sql'

test = open(path,'r').read()
process = re.sub('\s+',' ',test)
result = re.split(r'(SELECT|FROM|WHERE|HAVING)',process)
print(result)
select_no = [i for i, x in enumerate(result) if x=='SELECT']
from_no = [i for i, x in enumerate(result) if x=='FROM']
where_no = [i for i, x in enumerate(result) if x=='WHERE']
print(select_no)
if len(select_no) == 1:
    pass
elif len(select_no) > 1:
    rmPos = select_no[0]
    result = result[rmPos::]

print(result)        
# test = ['1.s','2','3','1','2']
# sample = ['1','2']
# print(all(a == ['1','2'] for a in test))
# print(type(test.count(1)))