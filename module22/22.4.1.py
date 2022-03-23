numbers = open("numbers.txt")
answer = 0

for i_elem in numbers:
    answer += int(i_elem)

numbers.close()
answer_file = open("answer.txt", 'w')
answer_file.write(str(answer) + "\n")
