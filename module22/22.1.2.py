import os


def print_dirs(path):
    for i_elem in os.listdir(path):
        print(os.path.abspath(os.path.join('..', i_elem)))


abs_path = os.path.abspath('..')
print_dirs(abs_path)
