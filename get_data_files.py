import numpy as np
import ast
import itertools
import re
import os
import sys

def fill_zeros(input_list, N):
    return input_list + [0.0] * (int(N) - len(input_list))

def pad_list_with_zeros(lists):
    max_len = max(len(lst) for lst in lists)
    return [lst + [0.0] * (max_len - len(lst)) for lst in lists]

def get_data_A(path): #Get matrix A, y convertirla en un array de listas
    # MatrixA=[]
    file=open(path+'/DS_MatrixA.txt','r') 
    lines = file.read().split("%")
    file.close()
    for line in lines:
        if line == '\n': break
        list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
        list = [float(i) for i in list]
        # MatrixA.append(list)
        file_input=open('tensors/A.txt','a') 
        file_input.write(str(list)+'\n')
#    return MatrixA
    


def get_data_B(path):
    # MatrixB=[]
    file=open(path+'/DS_MatrixB.txt','r') 
    lines=file.read().split('%')
    for line in lines:
        if line == '\n': break
        list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
        list= [float(i) for i in list]
        # MatrixB.append(list)
        file_input=open('tensors/B.txt','a') 
        file_input.write(str(list)+'\n')
    # return MatrixB



def get_data_X(path):
    # MatrixX=[]
    file=open(path+'/DS_MatrixX.txt','r')
    lines=file.read().split('%')
    for line in lines:
        if line == '\n': break
        list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
        list= [float(i) for i in list]
        # MatrixX.append(list)
        file_input=open('tensors/X.txt','a') 
        file_input.write(str(list)+'\n')
    # return MatrixX


def get_data_P(path):
    # MatrixP=[]
    file=open(path+'/DS_P.txt','r')
    lines = file.read().split("%")
    for line in lines:
        if line == '\n': break
        aux=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
        try:
            aux = [float(i) for i in aux]
        except ValueError:
            aux=0 #for when is empty P
        # MatrixP.append(aux)
        file_input=open('tensors/P.txt','a') 
        file_input.write(str(list)+'\n')
    # return MatrixP


def make_tensors(folder):
    tensorList=[]
    #unir las matrices en un tensor para luego entregarsela al input 
    with open(folder+'/A.txt','r') as A:
        MatrixA=A.read().split('\n')
    with open(folder+'/B.txt','r') as B:
        MatrixB=B.read().split('\n')
    with open(folder+'/X.txt','r') as X:
        MatrixX=X.read().split('\n')
    for a, x, b in zip(MatrixA, MatrixX, MatrixB):
        tensor = list(itertools.chain(a, x,b))
        tensorList.append(tensor)      
    tensorList=pad_list_with_zeros(tensorList)
    with open('tensor_input.txt','a') as input:
        for i in tensorList:
            input.write(str(i)+'\n')
    #return tensor_pad

def make_tensor_P(folder):
    
    list=get_data_P(folder)
    tensorP=pad_list_with_zeros(list)
        
    return tensorP



def read_file_as_lists_of_floats(path):
    result = []
    with open(path, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.strip().split()
            float_list = [float(x) for x in line]
            result.append(float_list)
    return result


def main(folder):
    #make files, reading the test results 
    os.system('mkdir tensors')
    get_data_A(folder)
    get_data_B(folder)
    get_data_X(folder)
    sys.stdout.flush()
    make_tensors('tensors')
    sys.stdout.flush()

main('test_results')