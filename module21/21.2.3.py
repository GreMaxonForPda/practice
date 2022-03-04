site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_elem(struct, elem):
    if elem in struct:
        return struct[elem]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_elem(sub_struct, elem)
            if result:
                break
    else:
        result = None

    return result


returned = find_elem(site, 'p')
if returned:
    print("Значение:", returned)
else:
    print("Такого ключа нет")
