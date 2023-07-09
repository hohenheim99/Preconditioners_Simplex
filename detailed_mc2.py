import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")
#This will ignore all DeprecationWarning warnings in your code.

criteria='MC-4'
path1='/home/nico/codes/benchmarks/MC-3/benchmark_Model_MC-3_10%.csv'
path2='/home/nico/codes/benchmarks/MC-3/benchmark_Model_MC-3_30%.csv'
path3='/home/nico/codes/benchmarks/MC-3/benchmark_Model_MC-3_50%.csv'
path4='/home/nico/codes/benchmarks/MC-3/benchmark_Model_MC-3_70%.csv'
path5='/home/nico/codes/benchmarks/MC-3/benchmark_Model_MC-3_90%.csv'

pd.options.display.float_format = '{:.3f}'.format

Default=pd.read_csv('/home/nico/codes/benchmarks/base/benchmark_Model_default_v2.csv')
Default['File'] = Default['File'].str.replace('for_dataset/', '').str.replace('.bch', '').str.replace('_', '\\_')
Default_grouped=Default.groupby('File')
average_time_Default = Default_grouped['Time'].mean()

# 10
p1 = pd.read_csv(path1)
p1['File'] = p1['File'].str.replace('for_dataset/', '').str.replace('.bch', '').str.replace('_', '\\_')
p1_group =p1.groupby('File')
avg_time_10 = p1_group['Time'].mean()
df1=average_time_Default.compare(avg_time_10,result_names=('Default Time', '10\% Time'),keep_shape=True,keep_equal=True)
df1['10\% - Diff Time'] = ((df1['10\% Time'] - df1['Default Time']) / df1['Default Time']) *100

# 20
p2 = pd.read_csv(path2)
p2['File'] = p2['File'].str.replace('for_dataset/', '').str.replace('.bch', '').str.replace('_', '\\_')
p2_group =p2.groupby('File')
avg_time_20 = p2_group['Time'].mean()
df2=average_time_Default.compare(avg_time_20,result_names=('Default Time', '20\% Time'),keep_shape=True,keep_equal=True)
df2['20\% - Diff Time'] = ((df2['20\% Time'] - df2['Default Time']) / df2['Default Time']) *100

# 30
p3 = pd.read_csv(path3)
p3['File'] = p3['File'].str.replace('for_dataset/', '').str.replace('.bch', '').str.replace('_', '\\_')
p3_group =p3.groupby('File')
avg_time_30 = p3_group['Time'].mean()
df3=average_time_Default.compare(avg_time_30,result_names=('Default Time', '30\% Time'),keep_shape=True,keep_equal=True)
df3['30\% - Diff Time'] = ((df3['30\% Time'] - df3['Default Time']) / df3['Default Time']) *100


# 40
p4 = pd.read_csv(path4)
p4['File'] = p4['File'].str.replace('for_dataset/', '').str.replace('.bch', '').str.replace('_', '\\_')
p4_group =p4.groupby('File')
avg_time_40 = p4_group['Time'].mean()
df4=average_time_Default.compare(avg_time_40,result_names=('Default Time', '40\% Time'),keep_shape=True,keep_equal=True)
df4['40\% - Diff Time'] = ((df4['40\% Time'] - df4['Default Time']) / df4['Default Time']) *100


# 50
p5 = pd.read_csv(path5)
p5['File'] = p5['File'].str.replace('for_dataset/', '').str.replace('.bch', '').str.replace('_', '\\_')
p5_group =p5.groupby('File')
avg_time_50 = p5_group['Time'].mean()
df5=average_time_Default.compare(avg_time_50,result_names=('Default Time', '50\% Time'),keep_shape=True,keep_equal=True)
df5['50\% - Diff Time'] = ((df5['50\% Time'] - df5['Default Time']) / df5['Default Time']) *100


desired_order = ['Default Time','10\% - Diff Time','20\% - Diff Time','30\% - Diff Time','40\% - Diff Time','50\% - Diff Time']

dataframes = [df1['10\% - Diff Time'], df2['20\% - Diff Time'], df3['30\% - Diff Time'], df4['40\% - Diff Time'], df5['50\% - Diff Time']]


concatenated_df = pd.concat(dataframes,axis=1)

# print(concatenated_df.to_string())
latex_table = concatenated_df.to_latex(float_format="%.3f",bold_rows=True,escape=False)
print(latex_table)
