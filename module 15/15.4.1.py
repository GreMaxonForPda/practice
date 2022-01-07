string = input('Введите строку: ')

new_string = []
count = 0

for i in list(string):
    if i == ':':
        new_string.append(';')
        count += 1
    else:
        new_string.append(i)

print('Новая строка:', ''.join(new_string), '\nКоличество замен:', count)