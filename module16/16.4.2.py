def program(): 
  global n_people, k_people
  output = []
  num = 1
  for i_people in range(1, n_people + 1, k_people):
    output.append(list(range(i_people, num + k_people)))
    num += k_people
  return output
      

n_people = int(input('Сколько человек всего? '))
k_people = int(input('Кол-во человек в команде? '))

if n_people % k_people != 0:
  print(f'{n_people} человек невозможно поделить на команды по {k_people} человек!')
else:
  print(f'Ответ: {program()}')
