user_str = input('Введите строку: ')

lower = 0
upper = 0

for i_elem in user_str:
    if i_elem.islower():
        lower += 1
    elif i_elem.isupper():
        upper += 1

if lower > upper:
    print('\nРезультат:', user_str.lower())
elif upper > lower:
    print('\nРезультат:', user_str.upper())
else:
    print('\nОдинаковое кол-во и тех и тех букв.')
    print('Результат:', user_str)
