a = int(input('Please enter the number: '))
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(m)

"""Видимо с математикой у меня все плохо,
использовал https://taskcode.ru/cycles/max-digit"""
