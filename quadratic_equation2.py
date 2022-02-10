import math

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

d = b*b - 4*a*c
print('Дискриминантата е d = ', d)

if d == 0:
    x = -b/(2*a)
    print('Уравнението има един реален корен')
    print('x = ', x)
elif d > 0:
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    print('Уравнението има два реални корена')
    print('x1 = ', x1)
    print('x2 = ', x2)
else:
    xr = -b/(2*a)
    xi = math.sqrt(math.fabs(d))
    print('Уравнението има два корена, комплексни числа')
    print('x1 = ', xr, '-i', xi)
    print('x2 = ', xr, '+i', xi)
