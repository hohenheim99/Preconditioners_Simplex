import os
import numpy as np
import re

def get_change(path):
    pass

def count_variables(path):
    variables_n=[]
    with open(path,'r') as file:
        lines=file.read().split('%')
        lines.pop()
        for line in lines:
            line=line.strip()
            if '()' in line:
                aux=0
                variables_n.append(aux)
            else:
                # temp=line.splitlines()
                # try: print(temp.pop())
                # except: pass
                aux=len(line.splitlines())
                variables_n.append(aux)
    
    return variables_n

if __name__ == "__main__":
    path=input('folder: ')
    P=count_variables(path+'/DS_P.txt')
    with open(path+'/ratio.txt','a') as file:
        for i in P:
            file.write(str(i)+'\n')