import numpy as np
import ast
import itertools
import re
import os
from os.path import exists
import pandas as pd
from datetime import datetime,timezone
import pytz


def convert_to_list(int_list):
    return [[num] for num in int_list]

def fill_zeros(input_list, N):
    return input_list + [0.0] * (int(N) - len(input_list))

def pad_list_with_zeros(lists):
    max_len = max(len(lst) for lst in lists)
    return [lst + [0.0] * (max_len - len(lst)) for lst in lists]

def get_data_P(path): #Reads data from data results
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

def make_tensor_P(folder): #Make tensors and filled with zeroes the P results. Depricated
    list=get_data_P(folder)
    tensorP=pad_list_with_zeros(list)
    return tensorP

def process_data_results(path): #take raw data results from Ibex, and make tensors in form of list. Also fill with zeroes until the max len value
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
        # pad_list=aux
        print('input dim',len(pad_list[0]))
        for i in aux:
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

def read_data(path): #Read all the data
    aux=[]
    with open(path,'r') as file:
        for line in file:
            line=line.strip('\n')
            aux.append(ast.literal_eval(line))
    return aux

def count_variables(path): #count number of rows of P matrix
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

def count_variables_n(path,n): #count number of rows of P matrix
    variables_n=[]
    count=0
    with open(path,'r') as file:
        lines=file.read().split('%')
        while count < n:
            for line in lines:
                line=line.strip()
                if '()' in line:
                    aux=0
                    variables_n.append(aux)
                else:
                    aux=len(line.splitlines())
                    variables_n.append(aux)
            count+=1
    return variables_n

def count_variables_bool(path): #count if simplex worked or not
    variables_n=[]
    with open(path,'r') as file:
        lines=file.read().split('%')
        for line in lines:
            line=line.strip()
            if '()' in line:
                aux=0
                variables_n.append(aux)
            else:
                aux=1
                variables_n.append(aux)
        
    return variables_n


def read_data_n(path,n): #Read N lines of the file 
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
            line=line.strip('\n')
            if len(line)<=n:
                aux.append(ast.literal_eval(line))
    return aux


def make_json_history(folder,data):
    hist_df = pd.DataFrame(data)
    hist_json_file =folder+'/history.json' 
    with open(hist_json_file, mode='w') as f:
        hist_df.to_json(f)

def save_model_summary(folder,config,acti_funs,model):
    with open(folder+'/config.txt','w') as fh:
        for key, value in config.items(): 
            fh.write('%s: %s\n' % (key, value))
        # fh.write("\n".join(str(item) for item in config))
        model.summary(print_fn=lambda x: fh.write(x + '\n'))
        fh.write("\n".join(str(item) for item in acti_funs))


def save_all(folder,config,acti_funs,model,data):
    # tz = pytz.timezone('Chile/Continental')
    # date_time=datetime.now(timezone.utc).astimezone(tz=tz).strftime('%d-%m-%Y_%H:%M')
    # folder=path+'/Results_'+date_time
    # os.system('mkdir '+folder)
    make_json_history(folder,data)
    save_model_summary(folder,config,acti_funs,model)
    





if __name__ == "__main__":
    folder=input('folder of raw data: ')
    if exists(folder+'/tensor_input.txt') is False and exists(folder+'/tensor_input.txt') is False: 
        process_data_results(folder)
    else: 
        print('tensors files already exist')


