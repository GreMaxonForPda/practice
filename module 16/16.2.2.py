moneyList = []
peopleCount = int(input('Сколько всего работников? '))

for i_count in range(peopleCount):
    moneyList.append(int(input('Зарплата ' + str(i_count + 1) + ' работника: ')))

while min(moneyList) <= 0:
    peopleCount -= 1
    moneyList.remove(0)

print('\nРаботников осталось:', peopleCount)
print('\nЗарплаты:', moneyList)