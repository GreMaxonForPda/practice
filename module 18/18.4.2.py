path = input('Путь к файлу: ')

disk = input('На каком диске должен лежать файл: ')
end = input('Требуемое расширение файла: ')

if not path.startswith(disk):
    print('\nФайл лежит не на том диске.')
elif not path.endswith(end):
    print('\nФайл имеет не то расширение.')
else:
    print('\nПуть корректен!')
