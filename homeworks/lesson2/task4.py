words = input('Please enter some words: ') # просим ввести слова
a = words.split(' ') # разделяем слова через сплит
for el in a: # создаем цикл фор для элементов в списке
    if len(el) > 10: # если длина больше 10
        el = el[0:10] # обрезаем по 10е
    print(el) # вывод элемента
