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
with open('test_results/DS_MatrixA.txt','r') as file:
    lines = file.read().split("%")
    for line in lines:
        aux=re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line)
        print(aux)
    
        


