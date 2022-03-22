contacts = dict()

while True:
    print('\nТекущие номера в телефонной книге:')
    if len(contacts) == 0:
        print('<Пусто>')
    else:
        for i_elem in contacts:
            print(i_elem, contacts[i_elem])

    name = input('\nВведите имя (000 для завершения программы): ')
    if name in contacts:
        print('Имя уже есть в списке. Нажмите 1 для изменения номера ({0})'.format(
            contacts[name]
        ), end=' ')
        if input() == '1':
            number = input('Введите номер абонента: ')
            contacts[name] = number
    elif name == '000':
        break
    else:
        number = input('Введите номер абонента: ')
        contacts[name] = number
