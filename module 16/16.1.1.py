zoo_list = ['lion', 'elephant', 'monkey', 'kangaroo']
i_elephant = zoo_list.index('elephant')
zoo_list.insert(i_elephant + 1, 'bear')
zoo_list.remove('elephant')

print('\nНовый список:', zoo_list)
