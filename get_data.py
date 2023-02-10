import numpy as np
import ast
# from interval import interval, inf, imath
import itertools
import re

def fill_zeros(input_list, N):
    return input_list + [0.0] * (int(N) - len(input_list))

def pad_list_with_zeros(lists):
    max_len = max(len(lst) for lst in lists)
    return [lst + [0.0] * (max_len - len(lst)) for lst in lists]

def get_data_A(path): #Get matrix A, y convertirla en un array de listas
   MatrixA=[]
   with open(path+'/DS_MatrixA.txt','r') as file:
    lines = file.read().split("%")
    for line in lines:
        if line == '\n': break
        list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
        list = [float(i) for i in list]
        MatrixA.append(list)
    return MatrixA
        


def get_data_B(path):
    MatrixB=[]
    with open(path+'/DS_MatrixB.txt','r') as file:
        lines=file.read().split('%')
        for line in lines:
            if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
            list= [float(i) for i in list]
            MatrixB.append(list)
    return MatrixB



def get_data_X(path):
    MatrixX=[]
    with open(path+'/DS_MatrixX.txt','r') as file:
        lines=file.read().split('%')
        for line in lines:
            if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
            list= [float(i) for i in list]
            MatrixX.append(list)
    return MatrixX


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


def make_tensors(folder):
    #unir las matrices en un tensor para luego entregarsela al input 
    MatrixA=get_data_A(folder)
    MatrixB=get_data_B(folder)
    MatrixX=get_data_X(folder)
    tensorList=[]
    if len(MatrixA) == len(MatrixB) and len(MatrixB) == len(MatrixX):
        for i in range(len(MatrixA)):
            # #MATRIX A
            # mA=MatrixA[i]
            # #MATRIX X 
            # mX=MatrixX[i]
            # #MATRIX B
            # mB=MatrixB[i]
            
            tensor = list(itertools.chain(MatrixA[i], MatrixX[i], MatrixB[i]))
            
            #filled_tensor=pad_list_with_zeros(tensor)
            tensorList.append(tensor)
            #MEDIR EL MAXIMO LEN DE LA LISTA
            
    else:
        print("Error in dataset")

    tensor_pad=pad_list_with_zeros(tensorList)
    return tensor_pad

def make_tensor_P(folder):
    
    list=get_data_P(folder)
    tensorP=pad_list_with_zeros(list)
        
    return tensorP

