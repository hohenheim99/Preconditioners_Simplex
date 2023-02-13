import numpy as np
import ast
import itertools
import re
import os
# from ibexopt_mass_solver import Mass_solver

def fill_zeros(input_list, N):
    return input_list + [0.0] * (int(N) - len(input_list))

def pad_list_with_zeros(lists):
    max_len = max(len(lst) for lst in lists)
    return [lst + [0.0] * (max_len - len(lst)) for lst in lists]

def get_data_P(path):
    MatrixP=[]
    with open(path+'/DS_P.txt','r') as file:
        lines = file.read().split("%")
        for line in lines:
            if line == '\n': break
            aux=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
            try:
                aux = [float(i) for i in aux]
            except ValueError:
                aux=0 #for when is empty P
            MatrixP.append(aux)
    return MatrixP

def make_tensor_P(folder):
    list=get_data_P(folder)
    tensorP=pad_list_with_zeros(list)
    return tensorP

def get_data(path):
    aux=[]
    os.system('mkdir tensors')
    with open(path+'/AXB.txt','r') as file:
        lines=file.read().split('%')
        for line in lines:
            if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
            list= [float(i) for i in list]
            aux.append(list)
    with open('tensors/tensor_input.txt','a') as input:
        pad_list=pad_list_with_zeros(aux)
        print('input dim',len(pad_list[0]))
        for i in pad_list:
            input.write(str(i)+'\n')
    aux.clear()
    with open(path+'/DS_P.txt','r') as file2:
        lines=file2.read().split('%')
        for line in lines:
            if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
            list= [float(i) for i in list]
            aux.append(list)
    with open('tensors/tensor_output.txt','a') as output:
        pad_list=pad_list_with_zeros(aux)
        print('output dim',len(pad_list[0]))
        for k in pad_list:
            output.write(str(k)+'\n')
            

def read_data(path):
    aux=[]
    with open(path,'r') as file:
        for line in file:
            line=line.strip('\n')
            aux.append(ast.literal_eval(line))
    return aux




folder='test_results'
# benchs=input("select folder of benchs: ")
# Mass_solver(benchs)
