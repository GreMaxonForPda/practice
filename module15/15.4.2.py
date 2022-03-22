userString = input('Введите строку: ')
userSymbol = int(input('Номер символа: '))

rightSymbol = ''
leftSymbol = ''
symbolCount = 0
tempList = list(userString)

for i in tempList:
    if i == tempList[userSymbol - 1]:
        symbolCount += 1

leftSymbol = tempList[userSymbol - 2]
rightSymbol = tempList[userSymbol]

print('\nСимвол слева:', leftSymbol , '\nСимвол справа:', rightSymbol)

if tempList[userSymbol - 1] == leftSymbol == rightSymbol:
    print('\nЕсть два таких же символа среди соседей.')
elif tempList[userSymbol - 1] == leftSymbol or tempList[userSymbol - 1] == rightSymbol:
    print('\nЕсть ровно один такойже символ среди соседей.')
else:
    print('\nТаких же символов нет среди соседей.')