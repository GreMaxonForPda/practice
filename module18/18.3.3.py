msg_celebrate = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')

if '{name}' not in msg_celebrate and '{age}' not in msg_celebrate:
    print('Ошибка! Одна или две конструкции не найдены')
else:
    name_list = input('Введите список ФИ через запятую: ').split(', ')
    age_list = input('Введите список возрастов через пробел: ').split()

    print()
    for i_num in range(len(name_list)):
        print(msg_celebrate.format(
            name=name_list[i_num],
            age=age_list[i_num]
        ))
