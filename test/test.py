import os,sys
import re
import numpy as np
path = 'P:\RESEARCH\SQL Jobs\GPA Calculation\TEST_TYPE.sql'

test = open(path,'r').read()

process = re.sub('\s+',' ',test).upper()
GetNestSQL = re.findall(r'\(([^)]*)\)',process)

# print(test)

# # next_test = re.sub(r'(?<=\(\bSELECT.*?\))','',process)
# # test2 = re.findall(r'',process)
# # test = re.findall(r'(?<=SELECT).*?(?=FROM)',next_test)
# print(GetNestSQL)

# nest_list = [x for x in GetNestSQL if 'SELECT' in x]
# # print(nest_list)
# # # print(test)
# # # print(len(test))
# # # print(process)
# # # print(next_test)
# # for x in nest_list:
# #     process_wo_nest = process.replace(x ,'')
# for i in range(0,len(nest_list)):
#     process = process.replace(nest_list[i],'NEST TABLE')


# # a = ['a','b','b','b','c','f']
# # b = [i+1 for i, x in enumerate(a) if x == 'b']
# # print(b)
# wo_nest = re.findall(r'(?<=SELECT).*?(?=FROM)',process) # without nest tables
# # nest_list = []
# # for i in range(len(nest_list)):
# #     process_field = re.findall(r'(?<=SELECT).*?(?=FROM)',nest_list[i]) 
# #     nest_list.append(process_field)
# field_dict = {}
# for i in range(len(wo_nest)):
#     field_dict[i] = wo_nest[i]
# for index, item in field_dict.items():
#     process_item = re.split(r',',item) 

# a = ['a']
# b = 'abdsf'
# for x in a:
#     if x in b:
#         print('t')
#     else:
#         print('f')

a ='SELECT * FROM FDG,DRSG'
c = re.split(r'(SELECT|FROM|WHERE|HAVING)',a)  
b = [i for i, x in enumerate(c) if x == 'SELECT']
print(c)
print(b)
if ',' in a:
    print('1')
else:
    print('2')

