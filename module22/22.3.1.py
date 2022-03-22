import os.path

file = open(os.path.abspath(os.path.join('task', 'group_1.txt')), 'r', encoding='utf-8')
summa = 0
diff = 0
compose = 1

for i_line in file:
    info = i_line.split()
    summa += int(info[2])
    diff -= int(info[2])

file.close()
file = open(os.path.abspath(os.path.join('task', 'Additional Info', 'group_2.txt')))

for i_line in file:
    info = i_line.split()
    compose *= int(info[2])

file.close()

print(f"Сумма очков первой группы: {summa}"
      f"\nРазность очков первой группы: {diff}"
      f"\nПроизведение очков второй группы: {compose}")
