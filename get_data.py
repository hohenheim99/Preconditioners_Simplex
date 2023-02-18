import numpy as np
import ast
import itertools
import re
import os
from os.path import exists
import pandas as pd


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

def process_data_results(path):
    aux=[]
    os.system('mkdir '+path+'_tensors')
    #INPUTS
    with open(path+'/AXB.txt','r') as file:
        lines=file.read().split('%')
        for line in lines:
            if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
            list= [float(i) for i in list]
            aux.append(list)
    with open(path+'_tensors/tensor_input.txt','a') as input:
        pad_list=pad_list_with_zeros(aux)
        print('input dim',len(pad_list[0]))
        for i in pad_list:
            input.write(str(i)+'\n')
    aux.clear()
    pad_list.clear()
    #OUTPUTS
    with open(path+'/DS_P.txt','r') as file2:
        lines=file2.read().split('%')
        for line in lines:
            if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
            list= [float(i) for i in list]
            aux.append(list)
    with open(path+'_tensors/tensor_output.txt','a') as output:
        pad_list=pad_list_with_zeros(aux)
        print('output dim',len(pad_list[0]))
        print('numbers of inputs/outputs',len(pad_list))
        for k in pad_list:
            output.write(str(k)+'\n')

def read_data(path):
    aux=[]
    with open(path,'r') as file:
        for line in file:
            line=line.strip('\n')
            aux.append(ast.literal_eval(line))
    return aux

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

def read_data_n(path,n):
    aux=[]
    with open(path,'r') as myfile:
        head = [next(myfile) for x in range(n)]
        for line in head:
            line=line.strip('\n')
            aux.append(ast.literal_eval(line))
    return aux

def read_data_even(path,n):
    aux=[]
    with open(path,'r') as myfile:
        for line in myfile:
            if len(line)<=n:
                line=line.strip('\n')
                aux.append(ast.literal_eval(line))
    return aux






if __name__ == "__main__":
    folder=input('folder of raw data: ')
    if exists(folder+'/tensor_input.txt') is False and exists(folder+'/tensor_input.txt') is False: 
        process_data_results(folder)
    else: 
        print('tensors files already exist')
