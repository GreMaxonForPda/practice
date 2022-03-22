number = int(input('Введите цифру: '))

new_dict = dict()

for i_num in range(1, number + 1):
    new_dict[i_num] = i_num ** 2
    print(i_num, '-', new_dict[i_num])
    