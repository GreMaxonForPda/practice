def key():
    name = input("{}Введите имя нового контакта: ".format(
        " " * 7
    ))
    surname = input("{}Введите фамилию нового контакта: ".format(
        " " * 7
    ))

    if input("{space}Все верно:  \n{space2}Имя - {nam}\n{space2}Фамилия - {sur}\n{space}Да/Нет: ".format(
        space=" " * 7,
        space2=" " * 11,
        nam=name,
        sur=surname,
    )) == "Да":
        return name, surname
    else:
        print()
        key()


def new_contact(phone_book):
    new_key = key()
    if new_key in phone_book:
        print("Данный контакт уже существует. Хотите изменить?", end=" ")
        if input() == "Да":
            number = int(input("Введите номер: "))
            return new_key, number
        else:
            print()
            key()
    else:
        number = int(input("Введите номер: "))
        return new_key, number


number_book = dict()
while True:
    print("На данный момент телефонная книга состоит из:")
    for i_key, i_elem in number_book.items():
        print("{space}{first} - {second}".format(
            space=" " * 7,
            first=i_key,
            second=i_elem
        ))
    print()
    if input("Хотите добавить новый номер? ") == "Да":
        temp_output = new_contact(number_book)
        number_book[temp_output[0]] = temp_output[1]
    else:
        break
