a = int(input('Левая граница: '))
b = int(input('Правая граница: '))

while a > b:
    print('Ошибка! Левая граница должна быть меньше правой...')
    a = int(input('Левая граница: '))
    b = int(input('Правая граница: '))

new_list = [i_num for i_num in range(a, b + 1) if i_num % 2 == 0]

print(f'\nЧетные числа в диапазоне {a, b}: {new_list}')
