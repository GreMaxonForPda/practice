import random


def list_create(iterable):
    list_dict = dict()
    for i_key, i_value in enumerate(iterable):
        list_dict[i_key] = i_value

    return list_dict


alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
first_list = (random.choice(alphabet) for _ in range(10))
second_list = (random.choice(alphabet) for _ in range(10))

print("Первый словарь: {}".format(
    list_create(first_list)
))
print("Второй словарь: {}".format(
    list_create(second_list)
))
