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

# sum
sum1 = 0
# sum = 0 + 5 = 5
# sum = 5 + 7 = 12
# sum = sum +  number <=> sum += number
for number in ll:
    sum1 += number
print(sum1)
print(sum(ll, 0))

# sum by condition
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

# count
print(len(ll))

# count by condition
cnt = 0
for number in ll:
    if number % 2 != 0:
        cnt += 1
if cnt == 0:
    print('No such data...')
else:
    print(cnt)

# min
minel = ll[0]
for number in ll:
    if number < minel:
        minel = number
print(minel)

print(min(ll))
print(max(ll))

# max by condition
init = False
for number in ll:
    if number < 0:
        if not init:
            maxel = number
            init = True
        elif number > maxel:
            maxel = number
if not init:
    print('No such data...')
else:
    print(maxel)

# min by condition
init = False
for number in ll:
    if number % 5 == 0:
        if not init:
            init = True
            minel = number
        elif number < minel:
            minel = number
if not init:
    print('No such data...')
else:
    print(minel)
