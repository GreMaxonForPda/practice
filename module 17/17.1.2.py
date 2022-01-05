joke_symbol = input('Введите доп.символ: ')

print('\n', '*' * 7, 'user input', '*' * 7)

user_string = input('\nВведите сообщение: ')

double_us = [i_symbol * 2 for i_symbol in user_string]
dus_and_js = [j_symbol + joke_symbol for j_symbol in double_us]

print('\nСписок удвоенных символов:', double_us, '\nСклейка с дополнительным символом:', dus_and_js)
