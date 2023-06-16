from multiprocessing import Process
import multiprocessing
import os
import subprocess
import csv
import pandas as pd
#--------------CONFIGURATION HALL -------------
seed_Inicial=1
seed_Final=1
timeout=3600
precision=0.001
criteria="model_mc1_2m_threshold_05"
path_to_benchs="/home/nico/codes/benchmarks/experiment_set.txt"
short='/home/nico/codes/benchmarks/short.txt'
ibexopt="/home/nico/Ibex/ibex-2.8.9/__build__/src/ibexopt"
csv_file="benchmarks/MC-2/benchmark_{0}.csv".format(criteria)
# ---------------------------------------------
# print("Number of cpu : ", multiprocessing.cpu_count())


def echo_sys(bench,seed_Inicial,seed_Final,timeout,ibexopt):
    results=[]
    for i in range(seed_Inicial,seed_Final+1):
        cmd="{0} {1} --random-seed={2} --timeout={3}".format(ibexopt,bench,i,timeout)
        output = subprocess.Popen( cmd, stdout=subprocess.PIPE, shell=True ).communicate()[0]
        print(bench+" "+str(i)+" done")
        output=output.decode("utf-8")
        output=output.split('\n') 
        results.append([bench,i,output[-2],timeout,output[-3],output[-4],output[-5],output[-6],output[-7]])
        
    df=pd.DataFrame(results)
    df.to_csv(csv_file, mode='a', index=False, header=False)

    
        

if __name__ == "__main__":  # confirms that the code is under main function
    files=[]
    with open(short,'r') as file:
        for line in file:
            files.append(line.strip('\n'))


    #create csv of benchmarks set
    headers=["File","Seed","Nodes",'Timeout',"Time","Relative precision","Simplex time","ANN time","Linearization time"]
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

    procs = []
    # instantiating process with arguments
    for file in files:
        proc = Process(target=echo_sys, args=(file,seed_Inicial,seed_Final,timeout,ibexopt,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()





