import os


def print_abspath(path, name):
    if os.path.exists(path):
        for i_folder in os.listdir(path):
            temp_path = os.path.join(path, i_folder, name)
            if os.path.exists(temp_path):
                print("    ", temp_path)
    else:
        print('Такой путь не найден')


abspath = os.path.abspath(os.path.join('..', '..', 'python_basic', 'Module21'))
file_name = 'main.py'
print_abspath(abspath, file_name)
