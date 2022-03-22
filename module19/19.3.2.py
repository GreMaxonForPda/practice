players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

for elem in players_dict.values():
    if elem.get('team') == 'A' and elem.get('status') == 'Rest':
        print('1.', elem.get('name', 'Haven`t Name'), end=' ')
    elif elem.get('team') == 'B' and elem.get('status') == 'Training':
        print('2.', elem.get('name', 'Haven`t Name'), end=' ')
    elif elem.get('team') == 'C' and elem.get('status') == 'Travel':
        print('3.', elem.get('name', 'Haven`t Name'), end=' ')
