import numpy as np
import ast
import itertools
import re
import os
from os.path import exists
import pandas as pd
from datetime import datetime,timezone
import pytz


def padd_to_n(main_list,n):
    return [lst + [0.0] * (n - len(lst)) for lst in main_list]


def fill_zeros(input_list, N): #depricated
    return input_list + [0.0] * (int(N) - len(input_list))

def pad_list_with_zeros(lists):
    max_len = max(len(lst) for lst in lists)
    return [lst + [0.0] * (max_len - len(lst)) for lst in lists]

def read_data_AXB_n(path,n):
    aux=[]
    with open(path+'/AXB.txt','r') as file:
        head= [next(file) for x in range(n)]
        for line in head:
            if line == '\n': break
            # list=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line) #old regex. Error with letter e
            list=re.findall("(?<=[AZaz])?(?!\d*=)[eE0-9.+-]+", line)
            list= [round(float(i),7) for i in list]
            aux.append(list)
    return aux  

def read_data_P_n(path,n):
    aux=[]
    with open(path+'/DS_P.txt','r') as file:
        head= [next(file) for x in range(n)]
        for line in head:
            # if line == '\n': break
            list=re.findall("(?<=[AZaz])?(?!\d*=)[eE0-9.+-]+", line)
            list= [round(float(i),7) for i in list]
            aux.append(list)
    return aux     

def read_data_width_n(path,n):
    aux=[]
    with open(path+'/intervals_change.txt','r') as file:
        head= [next(file) for x in range(n)]
        for line in head:
            # if line == '\n': break
            list = line.split()
            list= [round(float(i),7) for i in list]
            aux.append(list)
    return aux     

def get_data_AXB_variation(path,start,end):
    aux=[]
    with open(path+'/AXB.txt','r') as file:
        for line_number, line in enumerate(file):
            if start-1<=line_number and line_number<=end-1:
                list=re.findall("(?<=[AZaz])?(?!\d*=)[eE0-9.+-]+", line)
                list=[round(float(i),7) for i in list]
                aux.append(list)
    return aux



def read_data_width_n_variation(path,start,end):
    aux=[]
    with open(path+'/intervals_change.txt','r') as file:
        for line_number, line in enumerate(file):
            if start-1<=line_number and line_number<=end-1:
                list=line.split()
                list=[round(float(i),7) for i in list]
                aux.append(list)
    return aux   

def get_data_AXB_variation(path,start,end):
    aux=[]
    with open(path+'/DS_P.txt','r') as file:
        for line_number, line in enumerate(file):
            if start-1<=line_number and line_number<=end-1:
                list=re.findall("(?<=[AZaz])?(?!\d*=)[eE0-9.+-]+", line)
                list=[round(float(i),7) for i in list]
                aux.append(list)
    return aux


def make_json_history(folder,data): #deprecated
    hist_df = pd.DataFrame(data)
    hist_json_file =folder+'/history.json' 
    with open(hist_json_file, mode='w') as f:
        hist_df.to_json(f)

def save_model_summary(folder,config,model):
    with open(folder+'/config.txt','w') as fh:
        for key, value in config.items(): 
            fh.write('%s: %s\n' % (key, value))
        model.summary(print_fn=lambda x: fh.write(x + '\n'))


def save_all(folder,config,acti_funs,model,data): #deprecated
    make_json_history(folder,data)
    save_model_summary(folder,config,acti_funs,model)
    






   


