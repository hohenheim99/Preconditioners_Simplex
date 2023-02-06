import numpy as np
import ast
from interval import interval, inf, imath
import itertools


def delete_characters(a):
    characters =["((","))","(",")",";","\n"," "]
    for i in characters:
        if i ==";":
            a=a.replace(i,",")
        elif i =="((":
            a=a.replace(i,"[[")
        elif i =="))":
            a=a.replace(i,"]]")
        elif i =="(":
            a=a.replace(i,"[")
        elif i ==")":
            a=a.replace(i,"],")
        else:
            a=a.replace(i,"")

    return a
def fill_zeros(input_list, N):
    return input_list + [0] * (int(N) - len(input_list))

def check_max_size(list):
    pass
   


def get_data_A(path): #Get matrix A, y convertirla en un array de listas
    m_A = open(path, "r")
    lines = m_A.read().split("%")
    MatrixA=[]
    for line in lines:
        if line == "\n":
            break
        out=delete_characters(line)
        data=ast.literal_eval(out)
        #arr= [eval(i) for i in arr] #Para convertir de string a lista simple
        MatrixA.append(data)
    return MatrixA
#print(A.reshape(1,8))


def get_data_B(path):
    m_A = open(path, "r")
    lines = m_A.read().split("%")
    MatrixB=[]
    for line in lines:
        if line == "\n":
            break
        out=delete_characters(line)
        data=ast.literal_eval(out.replace("],","]"))
        MatrixB.append(data)
    return MatrixB



def get_data_X(path):
    m_A = open(path, "r")
    lines = m_A.read().split("%")
    MatrixX=[]
    for line in lines:
        if line == "\n":
            break
        out=line.replace(";",",")
        data=ast.literal_eval(out)
        MatrixX.append(data)
    return MatrixX


def get_data_P(path):
    pass
    m_A=open(path,"r")
    lines = m_A.read().split("%")
    MatrixP=[]
    for line in lines:
        if line=="\n":
            break
        out=delete_characters(line)
        data=ast.literal_eval(out)
        #arr= [eval(i) for i in arr] #Para convertir de string a lista simple
        MatrixP.append(data)
    return MatrixP


def make_tensors(folder,n):
    #paths
    pathA=folder+'/DS_MatrixA.txt'
    pathB=folder+'/DS_MatrixB.txt'
    pathX=folder+'/DS_MatrixX.txt'
    

    

    #unir las matrices en un tensor para luego entregarsela al input 
    MatrixA=get_data_A(pathA)
    MatrixB=get_data_B(pathB)
    MatrixX=get_data_X(pathX)
    tensorList=[]
    if len(MatrixA) == len(MatrixB) and len(MatrixB) == len(MatrixX):
        for i in range(len(MatrixA)):
            #MATRIX A
            mA=np.array(MatrixA[i])
            mA.flatten()
            mA=mA.tolist()
            #MATRIX B
            mB=np.array(MatrixB[i])
            mB.flatten()
            mB=mB.tolist()
            #MATRIX X 
            mX=np.array(MatrixX[i])
            mX.flatten()
            mX=mX.tolist()

            tensor = list(itertools.chain(mA, mB, mX))
            filled_tensor=fill_zeros(tensor,n)
            tensorList.append(filled_tensor)
            #MEDIR EL MAXIMO LEN DE LA LISTA
            
    else:
        print("Error in dataset")


    return tensorList



def make_tensor_P(folder,n):
    pathP=folder+'/DS_P.txt'
    tensor_P=[]
    list=get_data_P(pathP)
    for i in range(len(list)):
        mP=np.array(list[i])
        mP.flatten()
        mP=mP.tolist()
        mP=fill_zeros(mP,n)
        tensor_P.append(mP)
    
    return tensor_P


def get_A(path): 
    m_A = open(path, "r")
    lines = m_A.read().split("%")
    MatrixA=[]
    for line in lines:
        if line == "\n":
            break
        out=delete_characters(line)
        data=ast.literal_eval(out)
      
        MatrixA.append(data)
    return MatrixA

