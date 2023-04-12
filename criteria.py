import os
import numpy as np
import re
from get_data import read_data_P_n

def count_variables(path):
    variables_n=[]
    with open(path,'r') as file:
        for line in file:
            line=line.strip()
            if '()' in line:
                aux=0
                variables_n.append(aux)
            else:
                #aux=len(line.splitlines())
                aux=1
                variables_n.append(aux)
    
    return variables_n

def check_P(path,n):
    input=read_data_P_n(path,n)
    variables_n=[]
    for i in input:
        if bool(i):
            variables_n.append(1)
        else:
            variables_n.append(0)
    return variables_n

