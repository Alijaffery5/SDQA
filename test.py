import os


def trend_analysis():

    path = 'data\\phones.py'
    path2 = 'data\\test.py'

    with open(path, 'r') as file1:
        with open(path2, 'r') as file2:
            same = set(file2).symmetric_difference(file1)

    same.discard('\n')

    with open('NEW_FILE!!.txt', 'w') as file_out:
        for line in same:
            file_out.write(line)