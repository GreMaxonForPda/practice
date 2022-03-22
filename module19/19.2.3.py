string = input('Введите текст: ').lower()

hist = dict()
for x in string:
    if x in hist.keys():
        hist[x] += 1
    else:
        hist[x] = 1

for y in sorted(hist):
    print('{0}: {1}'.format(
        y,
        hist[y]
    ))

print('Максимальная частота: {}'.format(
    max(hist.values())
))
