incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

print('Общий доход равен', sum(incomes.values()))

temp_list = [min(incomes, key=incomes.get), min(incomes.values())]
print('Самый маленький доход у {0}. Он составляет {1} рублей'.format(
    temp_list[0],
    temp_list[1]
))
incomes.pop(temp_list[0])
print(incomes)