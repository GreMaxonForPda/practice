user_string = input("Введите строку: ")
print("Ответ: ", end="")
for i_index, i_elem in enumerate(user_string):
    if i_elem == "~":
        print(i_index, end=" ")
