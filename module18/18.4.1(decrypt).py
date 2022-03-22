def decrypt(msg, step):
    decrypt_msg = ''
    for i_elem in msg:
        if i_elem in alphabet:
            decrypt_msg += alphabet[(alphabet.index(i_elem) - step) % len(alphabet)]
        else:
            decrypt_msg += i_elem

    return decrypt_msg


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

crypt_msg = input('Введите текст для дешифрования: ').lower()
key = int(input('Введите ключ шифрования: '))

print('Расшифрованное сообщение:', decrypt(crypt_msg, key))
