users_seconds = input('Please enter number of seconds: ')
users_seconds = int(users_seconds)
users_hours = users_seconds // 3600
users_minutes = (users_seconds - users_hours * 3600) // 60
users_seconds = users_seconds - (users_hours * 3600 + users_minutes * 60)
print('This is {0}:{1}:{2}'.format(users_hours, users_minutes, users_seconds))