my_list = [11, 8, 8, 6, 4] # создали набор натуральных чисел
numb = int(input('Please enter the number: ')) # запрашиваем у пользователя номер
# создаем цикл фор для каждого элемента в списке
for el in my_list:
    if numb > el:
        my_list.insert(0, numb)
        break
    elif numb == el:
        a = my_list.index(numb)
        b = my_list.count(numb)
        my_list.insert(a + b, numb)
        break
    else:
        if numb < my_list[-1]:
            my_list.append(numb)
            break

print(my_list)