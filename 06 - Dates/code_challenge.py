from datetime import datetime, timedelta

# print today's date
today = datetime.now()
print(f' Hoy es {str(today)}')
# print yesterday's date
one_day = timedelta(days=1)
print(f'Ayer fue {str(today - one_day)}')

# ask a user to enter a date
date_entered = input('Enter a date(dd/mm/aaaa): ')
date = datetime.strptime(date_entered, '%d/%m/%Y')

# print the date one week from the date entered
print(str(date))