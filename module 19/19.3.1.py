family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8,
            'surname': 'Pipi'
        }
    ]
}

for i_elem in family_member.get('children', []):
    if i_elem.get('name', '') == 'Bob':
        print('Bob найден, его фамилия: {}'.format(
            i_elem.get('surname',  'Nosurname')
        ))
