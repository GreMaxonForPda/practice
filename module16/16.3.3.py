package_count = int(input('Сколько будет пакетов? '))
decode_package = []
temp = []
lost_package = 0

for i_number in range(package_count):
    print(f'\nПакет номер {i_number + 1}:')
    for i_temp in range(4):
        temp.append(int(input(f'{i_temp + 1} бит: ')))
    if temp.count(-1) > 1:
        print('Много ошибок в пакете!')
        lost_package += 1
    else:
        decode_package.extend(temp)
    temp = []

print(f'Полученное сообщение: {decode_package}')
print(f'Кол-во потерянных пакетов: {lost_package}')
print(f'Кол-во ошибок в пакете: {decode_package.count(-1)}')
