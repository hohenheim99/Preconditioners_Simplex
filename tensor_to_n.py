import os
import numpy as np
import re




def count_variables(path):
    variables_n=[]
    with open(path,'r') as file:
        lines=file.read().split('%')
        for line in lines:
            line=line.strip()
            if '()' in line:
                aux=0
                variables_n.append(aux)
            else:
                aux=len(line.splitlines())
                variables_n.append(aux)
        
    return variables_n

if __name__ == "__main__":
    path='test_results/DS_P.txt'
    list=count_variables(path)
    for i in list:
        print(i)