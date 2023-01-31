import glob, os
from pathlib import Path
import csv

#--------------CONFIGURATION HALL -------------
seed=3
timeout=1800
# ---------------------------------------------
def Mass_solver(path):
    i=0
    dataFull=[]
    root=os.getcwd()
    os.system("mkdir test_results")
    for path, subdirs, files in os.walk(path):
        for name in files:
            file=os.path.join(path, name)
            print(file)
            os.system("ibexopt --random-seed="+str(seed)+" --timeout="+str(timeout)+" "+file+" >> test_results/log.txt")
            #log reader
            with open("test_results/log.txt") as log:
                obj=["cells","time","simplex","linearization"]
                data=[file,seed]
                index=2
                lines=log.readlines()
                for word in obj:
                    for line in reversed(lines):
                        if word in line: 
                            temp=line.split(" ")
                            data.insert(index,temp[1].removesuffix("\n"))
                            index+=1
                            break
            #log reader
            dataFull.append(data)     
            #os.system("rm test_results/log.txt")

                
        print(dataFull)
        with open("benchmarkData.csv", "w", newline="") as f:
            header=["file","seed","nodes","time","linearization time","simplex time"]
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(dataFull)
                    
        

    # os.chdir(path+'/')
    # os.system("rm *.cov")
    # print("Archivos .COV borrados. Data almacenada en "+root+"/DS_Matrix[A/B/X/P].txt")


path=input("input path folder: ")
Mass_solver(path)
