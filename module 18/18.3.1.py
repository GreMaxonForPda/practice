found_str = []
for _ in range(int(input('Сколько будет слов? '))):
    found_str.append(input('Введите слово: '))

text = input('\nТекст: ')

print('\nПодсчет...')
for i_pair in range(len(found_str)):
    print('{0}: {1}'.format(
        found_str[i_pair],
        text.count(found_str[i_pair])
    ))
