import math


def size(r, h):
    side = 2 * math.pi * r * h
    full = side + 2 * (math.pi * r ** 2)

    return side, full


radius = float(input("Введите радиус: "))
high = float(input("Введите высоту: "))

output = size(radius, high)
print("Площадь боковой поверхности: {side}\nПолная площадь цилиндра: {full}".format(
    side=round(output[0], 3),
    full=round(output[1], 3)
))
