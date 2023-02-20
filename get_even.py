import os

def main(path):
    with open (path,'r') as file:
        aux=[]
        for line in file:
            line=line.strip('\n')
            aux.append(len(line))
    return aux


folder=''
main(folder)