def question(ask, error='Неправильный ответ. Введите (Да/Нет)', count=3):
    answer = input(ask)
    if answer == 'Да':
        return 1
    elif answer == 'Нет':
        return 1
    elif count - 1 > 0:
        count -= 1
        print(error, "\nКол-во попыток осталось:", count)
        question(ask, error, count)
    else:
        print('У вас больше не осталось попыток!')
        return 0


question('Вы хотите удалить файл? ')
