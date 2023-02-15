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
    list=count_variables('test_results/DS_P.txt')
    list2=count_variables('test_results/AXB.txt')
    with open('test_results/numbers.txt','a') as file:
        for i,k in zip(list2,list):
            try: aux=(k*100)/i

            except: aux=0
            file.write(str(i)+' '+str(k)+' '+str(aux)+'\n')