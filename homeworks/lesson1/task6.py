first_day_distance = int(input('Please enter distance of the first day: '))
goal_distance = int(input('Please enter your goal distance: '))
day = 1
while goal_distance >= first_day_distance:
    day += 1
    first_day_distance = first_day_distance * 1.1
print('At the day number {0}, our athlete have run more than {1}.'.format(day, goal_distance))