import json

file = open('countries.json')
countries = json.load(file)
# print(countries)

for country in countries:
    if country['name'][0].upper() == 'B':
        print(country)

for country in countries:
    if country['code'][0].upper() == 'B':
        print(country)

output = open('counries-out.json', 'w')
json.dump(countries, output, ensure_ascii=False, indent=4)

print(json.dumps(countries, indent=2))
print(json.dumps(countries, sort_keys=True, indent=2))

europe = json.load(open('europe.json'))
# print(europe)
# print(europe[0]['properties'])

for country in europe:
    if country['properties']['capital'][0].upper() == 'S':
        print(country)
