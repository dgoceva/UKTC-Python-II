numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers)
print(numbers[:])
print(numbers[2])
print(numbers[-4])
print(numbers[3:])
print(numbers[:5])

# numbers[3] = 101
# numbers.append(222)
# del numbers[3]

del numbers
# print(numbers)

t1 = (1, 2, 3, 'a', 'b', 'c', 'd', 'Hello tuple!', 2.3, 4.5, 7.1)
print(t1)

for t in t1:
    print(t)

for i in range(0, len(t1), 2):
    print(t1[i])

for i, v in enumerate(t1):
    print(i, '->', v)

t2 = tuple()

print(all(t2))
print(any(t2))

# None, False, '' === false in all() and any() funcitons
print(all(t1))
print(any(t1))

# print(min(t1))
t2 = (11, 12, -32, -4, 102, -121, 33)
print(min(t2))
print(max(t2))

# print(t2.min())

mint = 1
for t in t2:
    if t % 2 == 0:
        if mint == 1:
            mint = t
        elif mint > t:
            mint = t

print(mint)
