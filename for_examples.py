import sys

for x in range(10):  # 0 start, 1 step, 9 end -> (10-1)
    print(x)
for x in range(1, 11):  # [1,10], step = 1
    print(x, end=" ")
print()
for x in range(0, 10, 2):  # [0,9], step = 2
    print(x, end=" ")
print('\n'+50*'*')

print(ord('x'))
for ch in range(ord('a'), ord('z')+1):
    print(chr(ch), end=" ")
print('\n'+50*'*')

for x in range(1, 101):
    print(x, end=" ")
print('\n'+50*'*')

for x in range(1, 1001):
    if x % 10 == 7:
        print(x, end=" ")
print('\n'+50*'*')

l = []
n = int(input('n='))
for x in range(n):
    l.append(int(input()))
print(l)
print(sum(l))

sum_n = 0
n = int(input('n='))
for x in range(n):
    num = int(input())
    sum_n += num
print(sum_n)

max_num = None
n = int(input('n='))
for x in range(n):
    num = int(input())
    if max_num is None:
        max_num = num
    elif max_num < num:
        max_num = num
print(max_num)

max_num = -sys.maxsize-1
n = int(input('n='))
for x in range(n):
    num = int(input())
    if max_num < num:
        max_num = num
print(max_num)
