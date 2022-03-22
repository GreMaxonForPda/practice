# print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key]
# for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}
# if i_key % 2 == 0])

print([i_values for i_key, i_values in {0: 0, 1: 100, 2: 144, 3: 19}.items() if i_key % 2 == 0])
