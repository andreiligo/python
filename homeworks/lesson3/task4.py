def my_func1(x ,y):
    """Func via **"""
    return x ** y

print(my_func1(2, -2))
print(my_func1(6, -8))
print(my_func1(7, -3))
print(my_func1(2, -3))
print(my_func1(9, -8))
print(my_func1(3, -1))
print('=========================================')


def my_func2(x, y):
    """Func via while and *"""
    a = 1
    while a < abs(y):
        x = x * x
        a += 1
    return 1 / x


print(my_func1(2, -2))
print(my_func1(6, -8))
print(my_func1(7, -3))
print(my_func1(2, -3))
print(my_func1(9, -8))
print(my_func1(3, -1))