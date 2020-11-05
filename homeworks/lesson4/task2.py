my_list = [5, 8, 3, 2, 5, 5, 22, 5, 7]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)