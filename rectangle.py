x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))

a = max(x1, x2)-min(x1, x2)
b = max(y1, y2)-min(y1, y2)
print('a =', a)
print('b =', b)

S = (a*b)
P = 2*(a+b)

print('S= ', S)
print('P= ', P)
