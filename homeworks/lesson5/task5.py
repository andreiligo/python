with open("text5.txt", "w+") as file:
    list_base = '6 3 5 6 7 8 22 3'
    file.write(list_base)

file = open("text5.txt")
for line in file:
    list_2 = line.split()
    print(list_2)

new_list = []
for el in list_2:
    new_list.append(int(el))

print(sum(new_list))

file.close()
