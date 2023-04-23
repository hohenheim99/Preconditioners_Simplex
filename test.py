from get_data import *


folder='test_results'
start=10
end=20
list=get_data_AXB_variation(folder,start,end)

list=np.array(pad_list_with_zeros(list))


for i in list:
    print(i)
