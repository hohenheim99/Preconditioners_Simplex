import os

files_to_find = []
with open('files.txt') as fh:
    for row in fh:
        files_to_find.append(row.strip('\n'))

for file in files_to_find:
    os.system("cp "+file+ " benchs_dataset/selected/")