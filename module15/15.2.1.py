numbers = [3,7,5]
while True:
    number = int(input('Новое число: '))
    if number == 0:
        break
    numbers.append(number)
    print('Текущий список чисел:', numbers)
    for i in numbers:
        print(i ** 2, i ** 3, i ** 4)
    print()
