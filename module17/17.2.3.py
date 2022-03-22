prices_list = [float(input('Цена на товар: ')) for _ in range(5)]

first_year = int(input('\nПовышение цен на первый год: '))
second_year = int(input('Повышение цен на второй год: '))

first_list = [x * (1 + first_year / 100) for x in prices_list]
second_list = [x * (1 + second_year / 100) for x in prices_list]

print('\nСумма цен за каждый год:', round(sum(prices_list), 2),
      round(sum(first_list), 2),
      round(sum(second_list), 2))
