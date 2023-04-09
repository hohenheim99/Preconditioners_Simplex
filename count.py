import os

aux=0
with open("test_results/AXB.txt","r") as file:
    for line in file:
        aux+=1

print(aux)