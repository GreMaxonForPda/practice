import random

n_list = [random.randint(0, 20) for _ in range(20)]
a_num = random.randint(0, len(n_list))
b_num = random.randint(a_num, len(n_list))

print(f"Список чисел: {n_list} \nДлина списка: {len(n_list)}"
      f"\nЧисло А: {a_num}"
      f"\nЧисло В: {b_num}")

n_list[a_num:b_num] = []

print(f"\nСписок после удаления: {n_list} \nДлина списка: {len(n_list)}")
