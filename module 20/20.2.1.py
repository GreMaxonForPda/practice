import random

tuple_1 = tuple([random.randint(0, 5) for _ in range(10)])
tuple_2 = tuple([random.randint(-5, 0) for _ in range(10)])

tuple_1_2 = tuple(tuple_1 + tuple_2)
print(tuple_1_2, tuple_1_2.count(0))
