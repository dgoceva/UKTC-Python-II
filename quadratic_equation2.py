import matplotlib.pyplot as plt
import numpy as np
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

xplt = np.arange(-20, 20, 0.01)
yplt = a*xplt**2+b*xplt+c
plt.plot(xplt, yplt, color='darkblue', label='y=ax^2+bx+c')
yplt = xplt*xplt
plt.plot(xplt, yplt, color='magenta', label='y=x^2')
yplt = a*xplt+b
plt.plot(xplt, yplt, color='yellowgreen', label='y=ax+b')

plt.title('Графики на функции')
plt.xlabel('X', loc='right')
plt.ylabel('Y', loc='top', rotation=0)
plt.legend(loc='upper right', frameon=False)
plt.show()
