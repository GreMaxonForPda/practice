import random

list_1 = [random.randint(50, 80) for _ in range(10)]
list_2 = [random.randint(30, 60) for _ in range(10)]

list_3 = [('Погиб' if list_1[i_num] + list_2[i_num] > 100 else 'Выжил') for i_num in range(10)]

print(list_3)
