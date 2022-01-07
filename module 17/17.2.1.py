a = int(input('Левая граница: '))
b = int(input('Правая граница: '))

while a > b:
    print('Ошибка! Левая граница должна быть меньше правой...Попробуйте ещё раз')
    a = int(input('Левая граница: '))
    b = int(input('Правая граница: '))

first_list = [i_num ** 3 for i_num in range(a, b + 1)]
second_list = [i_num ** 2 for i_num in range(a, b + 1)]

print('\nСписок кубов чисел в диапазоне от 5 до 10:', first_list, '\nСписок квадратов чисел в диапазоне от 5 до 10:',
      second_list)
