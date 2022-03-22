import os.path


def print_info(path, filename='my_file.txt'):
    if os.path.exists(path):
        for i_elem in os.listdir(path):
            path_temp = os.path.join(path, i_elem, filename)
            if os.path.exists(path_temp):
                print(os.path.abspath(path_temp))
                if os.path.isdir(path_temp):
                    print("Это папка")
                elif os.path.isfile(path_temp):
                    print("Это файл\nРазмер файла:", os.stat(path_temp).st_size, "байт")
                elif os.path.islink(path_temp):
                    print("Это ссылка")
                break
        else:
            print("Объект не найден")
    else:
        print("Указанного пути не существует")


abs_path = os.path.abspath(os.path.join('..', '..', 'practice'))

print_info(abs_path)
