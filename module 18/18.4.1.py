def crypto(msg, step):
    encrypt_msg = ''
    for i_elem in msg:
        if i_elem in alphabet:
            encrypt_msg += alphabet[(alphabet.index(i_elem) + step) % len(alphabet)]
        else:
            encrypt_msg += i_elem

    return encrypt_msg


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

decrypt_msg = input('Введите текст для шифрования: ').lower()
key = int(input('Введите ключ шифрования: '))

print('Зашифрованное сообщение:', crypto(decrypt_msg, key))
