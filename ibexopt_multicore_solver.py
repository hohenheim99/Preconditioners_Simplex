from multiprocessing import Process
import multiprocessing
import os
import subprocess
import csv
#--------------CONFIGURATION HALL -------------
seed=1
timeout=
precision=0.001
criteria="Default"
threshold=0
path_to_benchs="/home/nico/codes/benchmarks/experiment_set.txt"
ibexopt="/home/nico/Ibex/ibex-2.8.9/__build__/src/ibexopt"
csv_file="benchmarks/benchmark_{0}_{1}_{2}.csv".format(criteria,seed,threshold)
# ---------------------------------------------
# print("Number of cpu : ", multiprocessing.cpu_count())


def echo_sys(bench,seed,timeout,ibexopt):
    cmd="{0} {1} --random-seed={2} --timeout={3}".format(ibexopt,bench,seed,timeout)
    output = subprocess.Popen( cmd, stdout=subprocess.PIPE, shell=True ).communicate()[0]
    print('done '+cmd)
    output=output.decode("utf-8")
    output=output.split('\n') 
    for i in range(len(output)):
        print(output[i]+" "+str(i))
    temp=[bench,seed,output[-2],timeout,output[-3],output[-4],output[-5],output[-6],output[-7]]
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(temp)
        

if __name__ == "__main__":  # confirms that the code is under main function
    files=[]
    with open(path_to_benchs,'r') as file:
        for line in file:
            files.append(line.strip('\n'))

    headers=["File","Seed","Nodes",'Timeout',"Time","Relative precision","Simplex time","ANN time","Linearization time"]

    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

    # files=files[:10]
    procs = []
    # instantiating process with arguments
    for file in files:
        proc = Process(target=echo_sys, args=(file,seed,timeout,ibexopt,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()





