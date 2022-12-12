days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


weekdays = [day for day in days if day[0] != 'S']
print(weekdays)
print(type(weekdays))


weekend = {day for day in days if day[0] == 'S'}
print(weekend)
print(type(weekend))
