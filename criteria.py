import os
import numpy as np
import re
from statistics import mean
from get_data import *


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

def bool_by_avg(path,n,avg): #Criteria: if % of interval changed is > avg defined
    list=makeAverage(path,n)
    for i in range(len(list)):
        if list[i] >= avg:
            list[i]=1
        else:
            list[i]=0
    return list


# def percentage_of_changed_intervals(path,n):
#     input=read_data_width_n(path,n)
#     percentage=[]
#     for i in input:
#         count = sum(1 for k in i if k > 0)
#         percentage.append((count/len(i))*100)
#     return percentage


# def bool_by_percentage(path,n,avg):
#     list=percentage_of_changed_intervals(path,n)
#     for i in range(len(list)):
#         if list[i]>=avg:
#             list[i]=1
#         else:
#             list[i]=0
#     return list