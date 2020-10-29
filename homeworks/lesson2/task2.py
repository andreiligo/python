element_count = int(input('Please enter the count ')) # запрашиваем к-во элементов
list = [] # создаем список
i = 0 # создаем переменную i для цикла while
element = 0 # создаем стартовый номер элемента
while i < element_count: # создаем цилк, указываем что i меньше количества элементов в списке
    list.append(input('Please enter the element ')) # добавляем элементы
    i += 1 # указываем шаг


for element in range(int(len(list)/2)): # создаем цикл for, указываем что в диапазоне к-тва эл-ов списка кратном 2
    list[element], list[element + 1] = list[element + 1], list[element] # указываем что эл + 1, эл = эл, эл + 1
    element += 1 # создаем шаг от номера элемента

print(list) # принтим список
















