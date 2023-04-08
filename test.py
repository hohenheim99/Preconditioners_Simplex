import os
import re


def read_data_AXB(path):
    aux=[]
    os.system('mkdir '+path+'_tensorsAXB')
    with open(path+'/AXB.txt','r') as file:
        for line in file:
            if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
            list= [float(i) for i in list]
            
            aux.append(list)
    return aux
            


def read_data_P(path):
    aux=[]
    with open(path+'/DS_P.txt','r') as file:
        for line in file:
            # if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
            list= [float(i) for i in list]
            
            aux.append(list)
    return aux     



input=read_data_AXB("test_results")
output=read_data_P("test_results")


for i,k in zip(input,output):
    print(i)
    print(k)
    print("%")
