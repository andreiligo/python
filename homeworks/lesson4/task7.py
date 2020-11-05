from itertools import count
from math import factorial


def gen_func():
    for el in count(1):
        yield factorial(el)


var_gen = gen_func()
x = 0
for i in var_gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break