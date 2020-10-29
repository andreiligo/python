dic1 = {12: 'winter',
         1: 'winter',
         2: 'winter',
         3: 'spring',
         4: 'spring',
         5: 'spring',
         6: 'summer',
         7: 'summer',
         8: 'summer',
         9: 'autumn',
         10: 'autumn',
         11: 'autumn'}
user_month = int(input('Please enter month number: '))
print(dic1.get(user_month))


# реализовываем через list
list1 = ['winter', 'spring', 'summer', 'autumn']
user_num = int(input('Please enter the number: '))
if user_num in (12, 1, 2):
    print(list1[0])
elif user_num in (3, 4, 5):
    print(list1[1])
elif user_num in (6, 7, 8):
    print(list1[2])
else:
    print(list1[3])