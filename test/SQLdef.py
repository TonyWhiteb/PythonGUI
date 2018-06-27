import os,sys
import re
import numpy as np
path = 'P:\RESEARCH\SQL Jobs\GPA Calculation\STEP1_STUDENT_ACAD_CRED.sql'

sql_query = open(path,'r').read()
process = re.sub('\s+',' ',sql_query)




class SQLprocess:

    def __init__(self, *args, **kwargs):
        self.sql_type = 'SIMPLE'
        self.SIMPLE_KEYWORDS = [' JOIN ']
        self.table_list = []
        self.field_list = []
        self.nest_list = []
        self.sql_wo_nest = None
        self.sql_query = re.sub('\s+',' ',sql_query).upper()
        # self.sql_wo_nest = re.sub(r'\((?=.* SELECT|SELECT)([^)]*)\)','',self.sql_query)
        # self.sql_query = re.sub(r'.*(?=SELECT)','SELECT',self.sql_query)
        # pre process
        self.first_level = re.split(r'(SELECT|FROM)',self.sql_query)
        # first split
        self.second_level = re.split(r'(SELECT|FROM|WHERE)',self.sql_query)
        # second split
        #NOTE: Using findall instead of split
        #NOTE: findall failed... unless I can write better regex...OTZ
        self.select_no = [i for i, x in enumerate(self.first_level) if x=='SELECT']
        self.from_no = [i for i, x in enumerate(self.first_level) if x=='FROM']
        # self.where_no = [i for i, x in enumerate(self.first_level) if x=='WHERE']
    def type_check(self,sql_query):
        for x in self.SIMPLE_KEYWORDS:
            if x in sql_query:
                self.sql_type = 'COMPLEX'
                return self.sql_type
            else:
                return self.sql_type
    
    def GetNestSQL(self,query_list):
        parenthese_list = re.findall(r'\(([^)]*)\)',query_list)
        self.nest_list = [x for x in parenthese_list if 'SELECT' in x]
        if len(self.nest_list) != 0:
            for i in range(len(self.nest_list)):
                query_list = query_list.replace(self.nest_list[i],self.nest_list[i],'')
            self.sql_wo_nest = query_list    
        else:
            self.sql_wo_nest = None
        return self.nest_list

    
    # def GetField(self,query_list):
    #     self.field_list = re.findall(r'(?<=SELECT).*?(?=FROM)',query_list)
    #     # TODO: Check if field_list is empty
    #     for i in range(self.field_list):
    #         if self.field_list[i] == '*':
    #             self.field_list[i] = 'ALL FIELDS'
    #     return self.field_list
    def GetField(self,sql_query):
        if self.type_check(sql_query) = 


    def GetTable(self,query_list):
        process_list = re.split(r'(SELECT|FROM|WHERE)',query_list)
        table_pos = [i+1 for i, x in enumerate(process_list) if x=='FROM']
        for pos in table_pos:
            self.table_list.append(process_list[pos])
        return self.table_list

    def ProcessField(self,field_list): # Using this for list after GetField()
        field_dict = {}
        # TODO: Check if field_list it empty
        for i in range(len(field_list)):
            field_dict[i] = field_list[i]
        for index, item in field_dict.items():
            if item != 'ALL FIELDS':
                process_item = re.split(r',',item) 
                








    
        
    
                

    