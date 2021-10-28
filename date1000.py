import datetime as dt

day = int(input('[01-31] '))
month = int(input('[01-12] '))
year = int(input('year: '))

input_date = dt.datetime(year, month, day)
print(input_date.strftime('%d-%m-%Y'))

result = input_date+dt.timedelta(days=1000)
print(result.strftime('%d-%m-%Y'))
