# import os,sys
# path = 'P:\RESEARCH\SQL Jobs\GPA Calculation\STEP1_STUDENT_ACAD_CRED.sql'

# test = open(path,'r').read()


test = ['1.s','2','3','1','2']
sample = ['1','2']
print(all(a == ['1','2'] for a in test))
print(type(test.count(1)))