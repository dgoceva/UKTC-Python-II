# import random
from random import randint
import numpy
# from numpy import mean


def calculate():
    a = int(input('a='))
    b = int(input('b='))
    print('a+b=', a+b)


def calculate1():
    a = int(input('a='))
    b = int(input('b='))
    return a + b


def calculate2(a, b):
    return a + b


def input_list():
    lst = []
    for i in range(-5, 5, 2):
        lst.append(i)
    return lst


def rand_list():
    lst = []
    for i in range(10):
        # lst.append(random.randint(-500, 500))
        lst.append(randint(-500, 500))
    return lst


# calculate()
# print('a+b=', calculate1())

# a1 = int(input('a='))
# b1 = int(input('b='))
# print('a+b=', calculate2(a1, b1))

ll = input_list()
print(ll)
print(len(ll))
print(max(ll), min(ll))


def average(data):
    if len(data) == 0:
        return 0
    else:
        return sum(data)/len(data)


ll1 = rand_list()
print(ll1)
print(len(ll1))
print(min(ll1), max(ll1))
print(sum(ll1), numpy.mean(ll1))
print(average(ll1))
print(average([]))
x = [a for a in range(10)]
print(x)
ll = [int(x) for x in input().split()]
print(ll)
ll = [x for x in input().split(',')]
print(ll)
ll2 = [x for x in ll1 if x < 0 and x % 2 == 0]
res = average(ll2)
print(round(res, 2))
print(round(average([x for x in ll1 if x < 0 and x % 2 == 0]), 2))
