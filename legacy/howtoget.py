import os 
from get_data import *
import re
import ast

folder="test_results"
pathA=folder+'/DS_MatrixA.txt'
pathB=folder+'/DS_MatrixB.txt'
pathX=folder+'/DS_MatrixX.txt'
pathP=folder+'/DS_P.txt'


list=[]
# temp=open("test.txt","a")
with open('test_results/DS_P.txt','r') as file:
    lines = file.read().split("%")
    for line in lines:
        if line == '\n': break
        temp=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
        #temp=re.findall("'[\d.]+",line)
        try:
            temp = [float(i) for i in temp]
        except ValueError:
            temp=0 #for when is empty P
        
        if type(temp) == "list":
            print(type(temp[0]))
        
        print(temp)
    
        
        
        
    
        


