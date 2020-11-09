file4 = open('text4.txt', 'r', encoding='utf-8')
sum_amount = 0
num_pers = 0
low_names = []
low_index = 20000
for line in file4:
    line_read = line.split()
    sum_amount += int(line_read[1])
    num_pers += 1
    money = int(line_read[1])
    if money <= low_index:
        low_names.append(line_read[0])


print(sum_amount / num_pers)
print(low_names)

file4.close()