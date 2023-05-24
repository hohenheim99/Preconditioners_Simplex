from multiprocessing import Process
import multiprocessing
import os
import time
import subprocess
import csv
#--------------CONFIGURATION HALL -------------
seed=1
timeout=10
precision=0.001
path_to_benchs="/home/nico/framework/old-instances-optim.txt"
ibexopt="/home/nico/Ibex/ibex-2.8.9/__build__/src/ibexopt"
# ---------------------------------------------
# print("Number of cpu : ", multiprocessing.cpu_count())

def echo_sys(bench,seed,timeout,ibexopt):
    cmd="{0} {1} --random-seed={2} --timeout={3}".format(ibexopt,bench,seed,timeout)
    print(cmd)
    output = subprocess.Popen( cmd, stdout=subprocess.PIPE, shell=True ).communicate()[0]
    output=output.decode("utf-8")
    output=output.split('\n') 
    temp=[bench,output[-3],output[-2]]
    with open("benchmarkData.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(temp)
        

if __name__ == "__main__":  # confirms that the code is under main function
    files=[]
    with open(path_to_benchs,'r') as file:
        for line in file:
            files.append(line.strip('\n'))

    headers=["File","Seed","Nodes",'Timeout',"Time","Relative precision","Ending status","Simplex time","ANN time","Linearization time"]

    with open("benchmarkData.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

    files=files[:10]
    procs = []
    # instantiating process with arguments
    for file in files:
        proc = Process(target=echo_sys, args=(file,seed,timeout,ibexopt,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()





