s1 = set()
print(s1)
s1 = {1, 2, 3, 4, 5, 6}
print(s1)
s1 = set([111, 121, 123])
print(s1)
s1 = set((211, 222, 233, 244, 255))
print(s1)

s2 = frozenset()
print(s2)
s2 = frozenset([11, 12, 12, 14])
print(s2)
s2 = frozenset((21, 22, 23))
print(s2)

print(len(s1))
print(len(s2))

s11 = s1.copy()
s22 = s2.copy()
print(s11, s22)
s3 = set(s22)
# s3[1] = [1, 2, 3]
s3.add(11)
s3.add(21)
# s3.add([1, 2, 3])
print(s3)
