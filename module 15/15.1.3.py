id_count = int(input('Введите кол-во сотрудников в офисе: '))
id_list = []

for _ in range(id_count):
    id_list.append(int(input('ID сотрудника: ')))

ask = int(input('\nКакого сотрудника ищем (ID)? '))

for _ in id_list:
    if _ == ask:
        temp = True
        break
    else:
        temp = False

if temp:
    print('Сотрудник на месте.')
else:
    print('Сотрудник не работает!')