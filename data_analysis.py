import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")
#This will ignore all DeprecationWarning warnings in your code.

criteria='MC-4'
path='/home/nico/codes/benchmarks/MC-4/benchmark_MC-4_full.csv'

pd.options.display.float_format = '{:.4f}'.format

Default=pd.read_csv('/home/nico/codes/benchmarks/base/benchmark_Model_default_v2.csv')
Criteria = pd.read_csv(path)
Criteria['File'] = Criteria['File'].str.replace('for_dataset/', '').str.replace('.bch', '').str.replace('_', '\\_')
Default['File'] = Default['File'].str.replace('for_dataset/', '').str.replace('.bch', '').str.replace('_', '\\_')
Default_grouped=Default.groupby('File')
Criteria_grouped =Criteria.groupby('File')

# Time
average_time_Default = Default_grouped['Time'].mean()
average_time_HC1 = Criteria_grouped['Time'].mean()
df=average_time_Default.compare(average_time_HC1,result_names=('Default Time', '{0} Time'.format(criteria)),keep_shape=True,keep_equal=True)
df['\% Diff Time'] = ((df['{0} Time'.format(criteria)] - df['Default Time']) / df['Default Time']) *100

# #Nodes
avg_nodes_Default=Default_grouped['Nodes'].mean()
avg_nodes_MC1=Criteria_grouped['Nodes'].mean()
df2=avg_nodes_Default.compare(avg_nodes_MC1,result_names=('Default Nodes', '{0} Nodes'.format(criteria)),keep_shape=True,keep_equal=True)
df2['\% Diff Nodes'] = ((df2['{0} Nodes'.format(criteria)] - df2['Default Nodes']) / df2['Default Nodes']) *100

# Precision
avg_precision_Default=Default_grouped['Relative precision'].mean()
avg_precision_MC1=Criteria_grouped['Relative precision'].mean()
df3=avg_precision_Default.compare(avg_precision_MC1,result_names=('Default Precision', '{0} Precision'.format(criteria)),keep_shape=True,keep_equal=True)
df3['\% Diff Precision'] = ((df3['{0} Precision'.format(criteria)] - df3['Default Precision']) / df3['Default Precision']) *100

print(df3.to_string())
desired_order = ['Default Time', 'Default Nodes','Default Precision', '{0} Time'.format(criteria), '{0} Nodes'.format(criteria),'{0} Precision'.format(criteria),'\% Diff Time','\% Diff Nodes','\% Diff Precision']

df_combined = pd.concat([df,df2,df3], axis=1)


df_final=df_combined.copy()
df_final = df_final.reindex(columns=desired_order)
df_final.columns = pd.MultiIndex.from_tuples([
    ('Default', 'Time'),
    ('Default', 'Nodes'),
    ('Default', 'Precision'),
    ('{0}'.format(criteria), 'Time'),
    ('{0}'.format(criteria), 'Nodes'),
    ('{0}'.format(criteria), 'Precision'),
    ('Comparison', '\% Diff Time'),
    ('Comparison', '\% Diff Nodes'),
    ('Comparison', '\% Diff Precision'),
], names=['Model', 'Metric'])
df_final.replace(np.nan, np.inf,inplace=True) 
latex_table = df_final.to_latex(float_format="%.4f",bold_rows=True,escape=False)
print(df_final.to_string())
print(latex_table)









