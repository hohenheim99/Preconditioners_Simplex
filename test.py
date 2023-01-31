import os 
from get_data import *


folder="test_results"
pathA=folder+'/DS_MatrixA.txt'
pathB=folder+'/DS_MatrixB.txt'
pathX=folder+'/DS_MatrixX.txt'
pathP=folder+'/DS_P.txt'

list1= get_data_P(pathP)

list2=get_data_A(pathA)

list3=get_data_B(pathB)

list4=get_data_X(pathX)

print(len(list1))
print(len(list2))
print(len(list3))
print(len(list4))

