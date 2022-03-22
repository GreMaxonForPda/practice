usr_input = input('Введите информацию о студенте через пробел\n '
                  '(имя, фамилия, город, место учёбы, оценки): ').split()

student = dict()
student['Имя'] = usr_input[0]
student['Фамилия'] = usr_input[1]
student['Город'] = usr_input[2]
student['Место учёбы'] = usr_input[3]
student['Оценки'] = []

for i_math in usr_input[4:]:
    student['Оценки'].append(i_math)

print()
for i_elem in student:
    print(i_elem, '-', student[i_elem])
