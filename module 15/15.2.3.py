scores_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

minimum = 0
maximum = 0
index = 0

for _ in scores_list:
    if scores_list[minimum] > _:
        minimum = index
    elif scores_list[maximum] < _:
        maximum = index
    index += 1

scores_list[minimum], scores_list[maximum] = scores_list[maximum], scores_list[minimum]

print('\n', scores_list)