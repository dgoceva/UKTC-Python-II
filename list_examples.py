import random

ll = []
for i in range(10):
    ll.append(i)
print(ll)

# ll = []
# for i in range(3):
#     ll.append(int(input('number: ')))
# print(ll)

ll = []
for i in range(10):
    ll.append(random.randint(-10, 100))
print(ll)

print(ll[3])
print(ll[2:5])
print(ll[:7])
print(ll[4:])

ll[2] = 105  # mutable
print(ll)
ll[1:3] = []
print(ll)
del ll[1:3]
print(ll)
ll[2:5] = [-1, -2, -3, -4, -5]
print(ll)
ll[4:6] = [-333]
print(ll)
# del ll[:]
# print(ll)
# del ll
# print(ll)

sum = 0
# sum = 0 + 5 = 5
# sum = 5 + 7 = 12
# sum = sum +  number <=> sum += number
for number in ll:
    sum += number
print(sum)

sum_positive = 0
for number in ll:
    if number > 0:
        sum_positive += number

if sum_positive == 0:
    print('No such data...')
else:
    print(sum_positive)

sum_even = 0
has_even = False
for number in ll:
    if number % 2 == 0:
        has_even = True
        sum_even += number

if not has_even:
    print('No even numbers...')
else:
    print(sum_even)
