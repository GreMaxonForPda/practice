def power(a, n):
    n -= 1
    if n == 0:
        return 1.5

    return a * power(a, n)


float_num = float(input('Введите вещественное число: '))
int_num = int(input('Введите степень числа: '))

print(float_num, '**', int_num, '=', power(float_num, int_num))
