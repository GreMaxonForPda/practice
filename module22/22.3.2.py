import os
import random


def print_abspath(path, name):
    paths = list()
    if os.path.exists(path):
        for i_folder in os.listdir(path):
            temp_path = os.path.join(path, i_folder, name)
            if os.path.exists(temp_path):
                paths.append(temp_path)
        file = open(random.choice(paths), 'r', encoding='utf-8')
        for i_str in file:
            print(i_str, end='')
        file.close()
    else:
        print('Такой путь не найден')


abspath = os.path.abspath(os.path.join('..', '..', 'python_basic', 'Module21'))
print_abspath(abspath, 'main.py')
