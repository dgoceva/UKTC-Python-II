import datetime as dt

current = dt.datetime.now()
print(current.strftime('%d-%m-%Y, %H:%M:%S'))

day = int(input('[01-31] '))
month = int(input('[01-12] '))
year = int(input('year: '))

input_date = dt.datetime(year, month, day)
print(input_date.strftime('%d-%m-%Y'))
