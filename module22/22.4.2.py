import os


def writer(path):
    statistic = open(os.path.join('statistic.txt'), 'a')
    for i_path in os.listdir(path):
        temp_path = os.path.join(path, i_path)
        if os.path.isdir(temp_path):
            for j_path in os.listdir(temp_path):
                temp_path_2 = os.path.join(temp_path, j_path, 'main.py')
                if os.path.exists(temp_path_2):
                    main_py = open(temp_path_2)
                    statistic.write(temp_path_2 + '\n')
                    statistic.write(main_py.read())
                    statistic.write('\n' + '*' * 40 + '\n')
                    main_py.close()
    statistic.close()


abs_path = os.path.abspath(os.path.join('..', '..', 'python_basic'))
if os.path.exists(abs_path):
    writer(abs_path)
