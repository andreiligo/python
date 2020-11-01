list1 = input('please enters some numbers: ')
t1 = tuple(int(item) for item in list1.split( ))
print(t1)
t1_sum = sum(t1)
print(t1_sum)
answer = input('Do you want to continue? Y/n: ')
if answer == 'n':
    exit()
else:
    list2 = input('Please enter new numbers: ')
t2 = tuple(list2.split( ))
print(t2)
for value in t2:
    try:
        t1_sum = t1_sum + int(value)
    except ValueError:
        print('Is not a number')

print(t1_sum)


# пытался переписать через функцию, не получилось, постоянно ловил ошибки и забил
# прошу скинуть как должна была выглядеть функция
