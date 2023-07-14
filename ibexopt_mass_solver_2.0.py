import subprocess
import csv
import pandas as pd

# seed=1
timeout=3600
precision=0.001
criteria="in_serie_Final_Final"
path_to_benchs="/home/nico/codes/benchmarks/experiment_set.txt"
short="/home/nico/codes/benchmarks/short.txt"
ibexopt="/home/nico/Ibex/ibex-2.8.9/__build__/src/ibexopt"
csv_file="/home/nico/codes/benchmarks/otros/benchmark_{0}.csv".format(criteria)



headers=["File","Seed","Nodes",'Timeout',"Time","Relative precision","Simplex time","ANN time","Linearization time"]
with open(csv_file, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)


files=[]
with open(short,'r') as file:
    for line in file:
        files.append(line.strip('\n'))

results=[]
for seed in range(1,5):
    for i in files:
        cmd = [ibexopt, str(i), f'--random-seed={seed}', f'--timeout={timeout}']
        output = subprocess.run(cmd, capture_output=True, text=True)
        output = output.stdout 
        # print(output)
        output=output.split('\n')
        results.append([i,seed,output[-2],timeout,output[-3],output[-4],output[-5],output[-6],output[-7]])
df=pd.DataFrame(results)
df.to_csv(csv_file, mode='a', index=False, header=False)