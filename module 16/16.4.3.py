goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

new_fruit = input('Новый фрукт: ')
new_price = int(input('Его цена: '))

goods.append([new_fruit, new_price])

print(f'Новый ассортимент: {goods}')

for i_price in range(len(goods)):
  goods[i_price][1] += goods[i_price][1] / 100 * 8
  
print(f'Ассортимент с новыми ценами: {goods}')
