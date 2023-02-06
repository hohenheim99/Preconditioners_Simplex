from get_data import *

folder='test_results'
n=100
input=make_tensors(folder,n)
output=make_tensor_P(folder,n)

input=input[:5]
output=output[:5]

for i in input:
    print(i)
    print('\n')
for i in output:
    print(i)
    print('\n')
