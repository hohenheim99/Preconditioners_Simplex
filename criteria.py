import os
import numpy as np
import re
from statistics import mean
from get_data import *

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

def check_if_P(path,n):
    input=read_data_P_n(path,n)
    variables_n=[]
    for i in input:
        if bool(i):
            variables_n.append(1)
        else:
            variables_n.append(0)
    return variables_n

def makeAverage(path,n):
    input=read_data_width_n(path,n)
    avg=[]
    for i in input:
        aux=mean(i)
        avg.append(aux)
    return avg

def bool_by_avg(list,avg):
    for i in range(len(list)):
        if list[i] >= avg:
            list[i]=1
        else:
            list[i]=0
    return list
            