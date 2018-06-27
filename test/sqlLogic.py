import os,sys
import re
import numpy as np
path = 'P:\RESEARCH\SQL Jobs\GPA Calculation\STEP1_STUDENT_ACAD_CRED.sql'

test = open(path,'r').read()
process = re.sub('\s+',' ',test).upper()
print(type(process))
# process2 = re.sub(r'.*(?=SELECT)','',process)
# print(process2)
process2 = process[process.index('SELECT'):]
result = re.split(r'(SELECT|FROM|WHERE|HAVING|LEFT JOIN|RIGHT JOIN|INNER JOIN|ON)',process2)
# print(result)
first_level = re.split(r'(SELECT|FROM)',process)
print('first:', first_level)
second_level = re.split(r'(SELECT|FROM|WHERE)',process)
print('second:',second_level)
select_no = [i for i, x in enumerate(result) if x=='SELECT']
from_no = [i for i, x in enumerate(first_level) if x=='FROM']
where_no = [i for i, x in enumerate(result) if x=='WHERE']
print(from_no)
print(where_no)
# print(select_no)
# print(from_no)
if len(select_no) == 1:
    pass
elif len(select_no) > 1:
    rmPos = select_no[0]
    result = result[rmPos::]
    for i in range(len(select_no)-1):
        if select_no[i+1] -select_no[i] < 3 or len(select_no) != len(from_no):
            print('No \'FROM\' between two \'SELECT\' statements?')
            #TODO: popup windows
        else:
            # select_arr = np.array(select_no)
            # from_arr = np.array(from_no)
            # field_no = (select_arr + from_arr)//2
            # #true division //
            # field_no = field_no.tolist()
            # field_no = list(map(operator.add,select_no,from_no))
            # field_no = [x / 2 for x in field_no]
            #FIX: Use numpy inead of this to be more faster
            field_list = []
            table_list = []
            for j in from_no:
                field_list.append(first_level[j-1])
            for k in from_no:
                table_list.append(result[k])

            print(field_list)
            print(table_list)         
              
#TODO: make a def ?




# print(result)    
# a = [1,2,3,4]
# b = a/2 
# print(b)   
# test = ['1.s','2','3','1','2']
# sample = ['1','2']
# print(all(a == ['1','2'] for a in test))
# print(type(test.count(1)))