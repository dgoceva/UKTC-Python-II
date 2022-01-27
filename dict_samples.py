import json

d = dict()
print(d)

# add/update
d['1'] = 'Ivan Ivanov'
d['2'] = 'Petyr Petrov'
d['3'] = 'Lili Marinova'
print(d)

# delete
d['1'] = ''
print(d)

del d['1']
print(d)

# del d
# print(d)

# retrieve
print(d['2'])
# print(d['1'])
print(d.get('1', None))
print(d.get('1', 'Inavlid Key'))
print(d.get('2', None))
print(d)
print(d.pop('2', None))
print(d)

d.clear()
print(d)

d = {'1': 'Ivan Ivanov', '2': 'Petyr Petrov', '3': 'Lili Marinova'}
print(d)
for k, v in d.items():
    print(k, '->', v)
print(d.keys())
print(d.values())

# json          <->         Python datatypes
# array         <->         list
# Number        <->         int,float
# String        <->         str
# true          <->         True
# false         <->         False
# null          <->         None
# Object        <->         dict
f = open('europe.json')
countries = json.load(f)
f.close()
# print(countries)
# print(countries[0])
# print(countries[0]['properties'])
# print(countries[0]['properties']['country'])
for country in countries:
    # print(country)
    # print(country['properties'])
    # print(country['properties']['country'])
    if country['properties']['country'][0].upper() == 'B':
        print(country['properties'])
    if country['properties']['capital'][0].upper() == 'S':
        print(country['properties'])
