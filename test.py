import os
import re
import ast


def read_data_P_n(path,n):
    aux=[]
    with open(path+'/DS_P.txt','r') as file:
        head= [next(file) for x in range(n)]
        for line in head:
            # if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
            list= [float(i) for i in list]
            aux.append(list)
    return aux     










# for i,k in zip(input,output):
#     print(i)
#     print(k)
#     print("%")
