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
            print(list)
            aux.append(list)
            


