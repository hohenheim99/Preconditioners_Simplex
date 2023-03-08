import os
import shutil
files_to_find = []
with open('files.txt') as fh:
    for row in fh:
        files_to_find.append(row.strip('\n'))

path='benchs'
end_folder='benchs/selected'

for root, dirs, files in os.walk(path):
    for file in files:
        if file in files_to_find:
            # If we find it, notify us about it and copy it it to C:\NewPath\
            print('Found file in: ' + str(root))
            shutil.copy(os.path.abspath(root + '/' + file), end_folder)
            files_to_find.remove(file)


for i in range(len(files_to_find)):
    print('falta: ',files_to_find[i])