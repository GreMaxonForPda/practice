user_line = tuple(input("Введите данные: ").split())

if type(user_line) == tuple or type(user_line) == str\
        or type(user_line) == int or type(user_line) == float\
        or type(user_line) == set:
    if type(user_line) == tuple:
        print("Тип данных: tuple")
    elif type(user_line) == str:
        print("Тип данных: str")
    elif type(user_line) == int:
        print("Тип данных: int")
    elif type(user_line) == float:
        print("Тип данных: float")
    elif type(user_line) == set:
        print("Тип данных: set")

    print("Неизменяемый (immutable)\nid объекта:", id(user_line))