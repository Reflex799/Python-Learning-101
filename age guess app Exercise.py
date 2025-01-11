from datetime import date

current_date = date.today()

current_year = current_date.year

print('Hello, welcome to my age guessing app. lets begin \n')

birth_year = int(input('what year were you born?'))

age = int(current_year - birth_year)

print(f'You are {age} years old.')