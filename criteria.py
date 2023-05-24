import os
import numpy as np
import re
from statistics import mean
from get_data import *

#Criteria: devuelve 1 si existe la matriz P
def check_if_P(path,n):
    input=read_data_P_n(path,n)
    variables_n=[]
    for i in input:
        if bool(i):
            variables_n.append(1)
        else:
            variables_n.append(0)
    return variables_n
#Crea un promedio de el % de cambio de los intervalos, en un nodo
def makeAverage(path,n):
    input=read_data_width_n(path,n)
    avg=[]
    for i in input:
        aux=mean(i)
        avg.append(aux)
    return avg

 #Criteria: devuelve bool=1 si un % de cambio promedio de los intervalos, es mayor o igual  un threshold: 
def bool_by_avg(path,n,threshold):
    list=makeAverage(path,n)
    for i in range(len(list)):
        if list[i] >= threshold:
            list[i]=1
        else:
            list[i]=0
    return list

#Criteria: devuelve bool=1 si un % de cambio de UN intervalo es mayor o igual  un threshold
def one_Interval_with_more_percentage(path,n,list,threshold): 
    list=read_data_width_n(path,n)
    for i in range(len(list)):
        if max(list[i]) >= threshold:
            list[i]=1
        else:
            list[i]=0
    return list
    
