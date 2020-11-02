def division_func(a: float, b: float) -> float:
    """Divine function of a and b"""
    if b == 0:
        print('Can not divide by zero')
        exit()  # как правильно выходить из программы в таком случае?
    return a / b

# Не смог решить через try except
# Скиньте плиз код в пример с решением через такой метод
# Как правильно выходить из программы? Прочитал что exit() для терминала только
print(division_func(5, 2))
print(division_func(5, 0))