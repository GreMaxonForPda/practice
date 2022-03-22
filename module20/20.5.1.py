data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

user_request = tuple(input("Введите серию и/или номер паспорта (через пробел): ").split())
for i_key, i_value in data.items():
    try:
        user_request = int(user_request[0]), int(user_request[1])
    except IndexError:
        user_request = int(user_request[0])
    except ValueError:
        print("\nПрограмма завершена с ошибкой!")
        break

    if user_request == i_key or user_request in i_key:
        print("Фамилия и имя: {name}".format(
            name=i_value
        ))
        break
