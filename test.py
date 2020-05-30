import os


path = 'C:\\Users\\alija\\OneDrive\\Desktop\\Frontend_V2\\data\\phones.py'
path2 = 'C:\\Users\\alija\\OneDrive\\Desktop\\Frontend_V2\\data\\tables.py'

with open(path, 'r') as file1:
    with open(path2, 'r') as file2:
        same = set(file1).difference(file2)

same.discard('\n')

with open('some_output_file.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)