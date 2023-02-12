import numpy as np
import ast
import itertools
import re
import os
from ibexopt_mass_solver import Mass_solver

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
    Matrix=[]
    os.system('mkdir tensors')
    with open(path+'/AXB.txt','r') as file:
        lines=file.read().split('%')
        for line in lines:
            if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
            list= [float(i) for i in list]
            Matrix.append(list)
            with open('tensors/tensor_input.txt','a') as input:
                input.write(str(list)+'\n')

    with open(path+'/DS_P.txt','r') as file2:
        lines=file2.read().split('%')
        for line in lines:
            if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
            list= [float(i) for i in list]
            with open('tensors/tensor_P.txt','a') as output:
                output.write(str(list)+'\n')


folder='test_results'
benchs=input("select folder of benchs: ")
Mass_solver(benchs)
get_data(folder)