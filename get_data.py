import numpy as np
import ast
import itertools
import re
import os
from os.path import exists
import pandas as pd
from datetime import datetime,timezone
import pytz



def fill_zeros(input_list, N): #depricated
    return input_list + [0.0] * (int(N) - len(input_list))

def pad_list_with_zeros(lists):
    max_len = max(len(lst) for lst in lists)
    return [lst + [0.0] * (max_len - len(lst)) for lst in lists]


def read_data_P(path): #read all the dataset
    aux=[]
    with open(path+'/DS_P.txt','r') as file:
        for line in file:
            # if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[eE0-9.+-]+", line)
            list= [float(i) for i in list]
            aux.append(list)
    return aux     


def read_data_AXB(path): #read all the dataset
    aux=[]
    with open(path+'/AXB.txt','r') as file:
        for line in file:
            if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[eE0-9.+-]+", line)
            list= [float(i) for i in list]
            aux.append(list)
    return aux     




def read_data_AXB_n(path,n):
    aux=[]
    with open(path+'/AXB.txt','r') as file:
        head= [next(file) for x in range(n)]
        for line in head:
            if line == '\n': break
            # list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line) #old regex. Error with letter e
            list=re.findall("(?<=[AZaz])?(?!\d*=)[eE0-9.+-]+", line)
            list= [float(i) for i in list]
            aux.append(list)
    return aux  

def read_data_P_n(path,n):
    aux=[]
    with open(path+'/DS_P.txt','r') as file:
        head= [next(file) for x in range(n)]
        for line in head:
            # if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[eE0-9.+-]+", line)
            list= [float(i) for i in list]
            aux.append(list)
    return aux     

def read_data_width_n(path,n):
    aux=[]
    with open(path+'/intervals_change.txt','r') as file:
        head= [next(file) for x in range(n)]
        for line in head:
            # if line == '\n': break
            list = line.split()
            list= [float(i) for i in list]
            aux.append(list)
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
    make_json_history(folder,data)
    save_model_summary(folder,config,acti_funs,model)
    






   


