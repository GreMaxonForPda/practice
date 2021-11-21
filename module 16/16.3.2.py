first_messages = input('Первое сообщение: ')
second_messages = input('Второе сообщение: ')

if first_messages.count('!') + first_messages.count('?') > second_messages.count('!') + second_messages.count('?'):
    print(first_messages, second_messages)
elif first_messages.count('!') + first_messages.count('?') < second_messages.count('!') + second_messages.count('?'):
    print(second_messages, first_messages)
else:
    print('Ой')
