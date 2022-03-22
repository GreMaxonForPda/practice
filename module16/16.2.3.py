def user_command(user_films, available_films, string):
    print('Доступные команды: удалить, вставить, добавить')
    command = input('Введите команду: ')
    if command == 'вставить':
        placing(user_films, available_films, string)
    elif command == 'удалить':
        removing(user_films, string)
    elif command == 'добавить':
        adding(available_films, user_films, string)
    else:
        print('Команда не распознана. Попробуйте еще раз.')
        user_command(user_films, available_films, string)


def removing(user_films, string):
    if string in user_films:
        user_films.remove(string)
    else:
        print('Такого фильма нет в вашем списке.')


def adding(available_films, user_films, string):
    # string = input('Введите название фильма: ')
    if string in available_films:
        if string in user_films:
            print('Ошибка. Фильм уже есть в вашем списке.')
        else:
            user_films.append(string)
    else:
        print('Такого фильма нет на сайте.')


def placing(user_films, available_films, string):
    if string in available_films:
        if string in user_films:
            print('Фильм уже есть в вашем списке.')
        else:
            user_index = int(input('На какое место вставить фильм? '))
            if user_index - 1 >= len(user_films):
                user_films.append(string)
                print('Фильм был добавлен в конец списка, т.к. введеное мместо находится за пределами списка.')
            user_films.insert(string, user_index - 1)
    else:
        print('Такого фильма нет на сайте.')


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня',
         'Проклятый остров', 'Начало', 'Матрица']
loving_films = []

print('Ваш текущий топ фильмов:', loving_films)
user_film = input('Введите название фильма: ')
user_command(loving_films, films, user_film)
while True:
    print('\nВаш текущий топ фильмов:', loving_films)
    user_film = input('Введите название фильма (quit для окончания работы): ')
    if user_film == 'quit':
        print('Программа успешно завершена.')
        break
    else:
        user_command(loving_films, films, user_film)
