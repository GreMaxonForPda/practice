user_string = {658: "rjk", 'i': 90, "jgl": 5}
print("Вывод: ", end="")
if isinstance(user_string, dict):
    for i_index, i_value in enumerate(user_string):
        if i_index % 2 == 0:
            print("{}: {}".format(
                i_value,
                user_string[i_value]
            ), end="\n" + " " * 7)
else:
    for i_index, i_value in enumerate(user_string):
        if i_index % 2 == 0:
            print(i_value, end="\n" + " " * 7)
