def check(string):
    for i_okt in string:
        if int(i_okt) > 255 or int(i_okt) < 0:
            return False

    return True


print('Пример правильного адреса: 192.168.1.0 \nПример неправильного адреса: 192.168.300.0')
user_str = input('\nВведите ip адрес (разделяя пробелами): ').split()
ip_address = '{first}.{second}.{third}.{four}'

if check(user_str):
    print('\nГотовый ip адрес: ', ip_address.format(
        first=user_str[0],
        second=user_str[1],
        third=user_str[2],
        four=user_str[3]
    ))
else:
    print('Обнаружена ошибка! программа будет завершена.')
