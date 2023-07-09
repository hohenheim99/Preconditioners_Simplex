import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")


pd.options.display.float_format = '{:.4f}'.format

# mc2='/home/nico/codes/benchmarks/MC-2/'
mc3='/home/nico/codes/benchmarks/MC-3/'

csv=['benchmark_Model_MC-3_10%.csv','benchmark_Model_MC-3_30%.csv','benchmark_Model_MC-3_50%.csv','benchmark_Model_MC-3_70%.csv','benchmark_Model_MC-3_90%.csv']
promedios=[]
for i in csv:
    Criteria = pd.read_csv(mc3+i)
    Criteria['File'] = Criteria['File'].str.replace('for_dataset/', '').str.replace('.bch', '').str.replace('_', '\\_')
    Criteria_grouped =Criteria.groupby('File')
    mean_values = Criteria_grouped['Nodes','ANN time'].mean()
    mean_values['division'] = mean_values['ANN time'] / mean_values['Nodes']

    mean_division = mean_values['division'].mean()
    rounded_mean_division = round(mean_division, 5)
    promedios.append(rounded_mean_division)
  

for i in promedios:
    print(i)


