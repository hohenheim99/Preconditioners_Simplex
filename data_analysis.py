import pandas as pd 
import matplotlib.pyplot as plt
import dataframe_image as dfi
import numpy as np

pd.options.display.float_format = '{:.3f}'.format
Criteria = pd.read_csv('/home/nico/codes/benchmarks/MC-2/benchmark_model_mc1_2m_threshold_05.csv').replace(np.inf,np.nan, regex=True)
Default=pd.read_csv('/home/nico/codes/benchmarks/base/benchmark_Default.csv').replace(np.inf,np.nan, regex=True)
Criteria['File'] = Criteria['File'].str.replace('for_dataset/', '')
Default['File'] = Default['File'].str.replace('for_dataset/', '')



Default_grouped=Default.groupby('File')
Criteria_grouped =Criteria.groupby('File')




col=['Time', 'Nodes','ANN time']

df1 = Default_grouped[col].mean()
df2 = Criteria_grouped[col].mean()

df_combined = pd.concat([df1.add_suffix('_Default'), df2.add_suffix('_Modelo')], axis=1)


desired_order = ['Time_Default', 'Time_Modelo','Time_Modelo without ANN', 'Nodes_Default','Nodes_Modelo','ANN time_Default','ANN time_Modelo']
df_combined['Time_Modelo without ANN'] = (df_combined['Time_Modelo'] - df_combined['ANN time_Modelo'])
# Reorder the columns based on the desired order
df_ordered = df_combined.reindex(columns=desired_order)

print(df_ordered.to_latex(index=True,formatters={"name": str.upper},float_format="{:.3f}".format,bold_rows=True))

# columns=['File','Relative precision']
# df_pre = pd.DataFrame(Criteria, columns=columns)
# print(df_pre.to_string())










# # Time
# average_time_Default = Default_grouped['Time'].mean()
# average_time_HC1 = Criteria_grouped['Time'].mean()
# df=average_time_Default.compare(average_time_HC1,result_names=('Default', 'MC-1'),keep_shape=True)
# df['percentage_change'] = ((df['MC-1'] - df['Default']) / df['Default']) *100
# df.name='Default vs MC-1: Time'
# print('------------------------')
# print(df.name)
# print(df)


# #Nodes
# avg_nodes_Default=Default_grouped['Nodes'].mean()
# avg_nodes_MC1=Criteria_grouped['Nodes'].mean()
# df2=avg_nodes_Default.compare(avg_nodes_MC1,result_names=('Default', 'MC-1'),keep_shape=True)
# df2['percentage_change'] = ((df2['MC-1'] - df2['Default']) / df2['Default']) *100
# df2.name='Default vs MC-1: Nodes'
# print('------------------------')
# print(df2.name)
# print(df2)



# avg_precision_Default=Default_grouped['Relative precision'].mean()
# avg_precision_MC1=Criteria_grouped['Relative precision'].mean()
# df3=avg_precision_Default.compare(avg_precision_MC1,result_names=('Default', 'MC-1'),keep_shape=True)
# df3['percentage_change'] = ((df3['MC-1'] - df3['Default']) / df3['Default']) * 100
# df3.name='Default vs MC-1: Precision'
# print('------------------------')
# print(df3.name)
# print(df3)



