import os
import re
import ast
import get_data



def check_P(path,n):
    input=read_data_P_n("test_results",10000)
    variables_n=[]
    for i in input:
        if bool(i):
            variables_n.append(1)
        else:
            variables_n.append(0)
    return variables_n





