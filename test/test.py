import os,sys
import re
path = 'P:\RESEARCH\SQL Jobs\GPA Calculation\STEP1_STUDENT_ACAD_CRED.sql'

test = open(path,'r').read()
result = re.split('^(?:SELECT|FROM|WHERE|HAVING)$',test)
print(result)
# test = ['1.s','2','3','1','2']
# sample = ['1','2']
# print(all(a == ['1','2'] for a in test))
# print(type(test.count(1)))