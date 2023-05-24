import glob, os
from pathlib import Path
import csv

#--------------CONFIGURATION HALL -------------
seed=1
timeout=1600
precision=0.001
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
            os.system("ibexopt --random-seed="+str(seed)+" --abs-eps-f="+str(precision)+"  --rel-eps-f="+str(precision)+" --timeout="+str(timeout)+" "+file+" >> test_results/log.txt")
            #log reader
            with open("test_results/log.txt") as log:
                obj=["cells","time","absolute_precision","relative_precision","status","simplex","red_time","linearization"]
                data=[file,seed]
                index=2
                lines=log.readlines()
                for word in obj:
                    for line in reversed(lines):
                        if word in line: 
                            temp=line.split(":")
                            data.insert(index,temp[1].removesuffix("\n"))
                            index+=1
                            break
            #log reader
            dataFull.append(data)     
            # os.system("rm test_results/log.txt")

                
        print(dataFull)
        # choice=input("Create csv? (Y / N): ")
        choice = "y"
        if choice.lower() == "y":
            with open("benchmarkData.csv", "w", newline="") as f:
                header=["File","Seed","Nodes","Time","Absolute precision","Relative precision","Ending status","Simplex time","ANN time","linearization time"]
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(dataFull)


                   
        



path=input("input path folder: ")
Mass_solver(path)
