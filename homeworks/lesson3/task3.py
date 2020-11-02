def my_func(a: float, b: float, c: float) -> float:
    """Function looks for sum of max numbers"""
    list1 = [a, b, c]
    list1.remove(min(list1))
    return sum(list1)

print(my_func(8, 3, 11))