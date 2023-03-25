import os

path=input("folder: ")
os.system("mkdir clean_benchs")
for root, dirs, files in os.walk(path):
    for file in files:
        with open(file, 'r') as infile, \
            open("clean_benchs/"+file, 'w') as outfile:
                data = infile.read()
                data = data.replace("(", "")
                data = data.replace(")","")
                outfile.write(data)
