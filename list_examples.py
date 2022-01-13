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

# average
sum1 = 0
for num in ll:
    sum1 += num
if len(ll) == 0:
    print('No such data...')
else:
    print('Average data: ', sum1/len(ll))

# average by condition
sum1 = 0
cnt = 0
size = min(len(ll), 5)
for i in range(size):
    sum1 += ll[i]
    if ll[i] != 0:
        cnt += 1
if cnt == 0:
    print('No such data...')
else:
    print('Average: ', sum1/cnt)

sum1 = 0
cnt = 0
for num in ll:
    if abs(num) % 10 == 4:
        sum1 += num
        cnt += 1
if cnt == 0:
    print('No more data...')
else:
    print('Average: ', sum1/cnt)

# generate list
result = []
for num in ll:
    result.append(num*2)
print(ll)
print(result)

# generate by condition
result = []
for num in ll:
    if abs(num) % 10 == 4:
        result.append(num)
print(result)

ll.sort()
print(ll)
ll.sort(reverse=True)
print(ll)

# bubble sort
print(ll)
ready = False
while not ready:
    end_index = len(ll) - 1
    ready = True
    for i in range(end_index):
        if ll[i] > ll[i+1]:
            temp = ll[i]
            ll[i] = ll[i+1]
            ll[i+1] = temp
            ready = False
            # ll[i],ll[i+1] = ll[i+1],ll[i]  # python works only
    end_index = end_index - 1
print(ll)

# selection sort
print(ll)
for i in range(len(ll)-1):
    maxi = i
    for j in range(i+1, len(ll)):
        if ll[maxi] < ll[j]:
            maxi = j
    ll[maxi], ll[i] = ll[i], ll[maxi]
print(ll)
