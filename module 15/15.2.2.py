numbers_count = int(input('Сколько будет чисел? '))
numbers_list = []
summ_indexes = 0

for _ in range(numbers_count):
    temp = int(input('Введите ' + str(_ + 1) + ' число: '))
    numbers_list.append(temp)

divider = int(input('\nВведите делитель: '))
print()

for _ in range(numbers_count):
    if numbers_list[_] % divider == 0:
        print('Индекс числа ' + str(numbers_list[_]) + ':', _)
        summ_indexes += _

print('Сумма индексов:', _)