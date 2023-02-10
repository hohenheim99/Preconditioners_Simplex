from get_data import *

folder='test_results'

list=make_tensor_P(folder)

list=list[:10000]
aux=[]
for i in list:
    for k in i:
        if type(k)!=float: print(type(k))
            
