# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# age = int(input('please enter your age:'))
# if age >= 18:
#     print('可以开车了')
# else:
#     print('滴，儿童卡')
# print('''hehe
# \nhaha
# xixi''')
# n = 123
# f = 456.789
# s1 = 'hello, world'
# s2 = 'hello, \'adam\''
# s3 = r'hello, "bart"'
# s4 = r'''hello,
# lisa!'''
# print(n, f, s1, s2, s3, s4)
# s1 = 72
# s2 = 85
# rate = (s2 - s1) / s1 * 100
# print('成绩提升了: %.1f %%' % rate) 

# weight = float(input('请输入您的体重(kg): '))
# height = float(input('请输入您的身高(m): '))
# bmi = weight / (height**2)
# str = ''
# if bmi < 18.5:
#     str = '过轻'
# elif bmi <= 25:
#     str = '正常'
# elif bmi <= 28:
#     str = '过重'
# elif bmi <= 32:
#     str = '肥胖'
# else:
#     str = '严重肥胖'
# print('您的bmi指数为: %.1f, 属于%s' % (bmi, str))

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#     print('hello, %s' % x)

# n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n = n + 1
# print('end')

# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0:
#         continue
#     print(n)
# print('end')

# while True:
#     print('11')

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# n = input('请输入数字: ')
# my_abs(n)

# import math
# def quadratic(a, b, c):
#     a = int(a)
#     b = int(b)
#     c = int(c)
#     m1 = b*b / (4*a*a) - (c/a)
#     if m1 < 0:
#         raise TypeError('输入的参数无法计算')
#     m = math.sqrt(m1)
#     n = b / (2*a)
#     x1 = m - n
#     x2 = -m - n
#     return x1, x2
# a = input('请输入一元二次方程的三个数a: ')
# b = input('请输入一元二次方程的三个数b: ')
# c = input('请输入一元二次方程的三个数c: ')
# print(quadratic(a, b, c))

# def power(x, n=2):
#     return x**n
# print('结果为:', power(5, 3))

# def enroll(name, gender, age=6, city='北京'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n*n
#     return sum

# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'others:', kw)

# def person(name, age, *args, city, job):
#     print('name:', name, 'age:', age, 'args:', args, 'city:', city, 'job:', job)

# def f1(a, b, c=0, *args, **kw):
#     print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

# def f2(a, b, c=0, *, d, **kw):
#    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)

# def fact(n):
#     if n == 0:
#         return 1
#     elif n < 0:
#         raise TypeError('暂不考虑负数的阶乘')
#     else:
#         return n * fact(n-1)

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# 汉诺塔
# def move(n, a='A', b='B', c='C'):
#     if n == 0:
#         raise TypeError('盘子数不能为0')
#     elif n == 1:
#         print(a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         print(a, '-->', c)
#         move(n-1, b, a, c)

# d = {'a': 1, 'b': 2, 'c': 3}
# for key, value in d.items():
#     print(key, ':', value)

# ary = [1, 2, 3, 4]
# for i, value in enumerate(ary):
#     print(i, value)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# g= fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

# def triangles():
#     n, lx, ly = 1, [], [1]
#     while True:
#         yield(ly)
#         lx = ly[:]
#         m = n + 1
#         ly = list(range(m))
#         for i in range(m):
#             if i - 1 < 0:
#                 ly[i] = lx[i]
#             elif i + 1 == m:
#                 ly[i] = lx[i-1]
#             else:
#                 ly[i] = lx[i] + lx[i-1] 
#         n = n + 1

# 更加简洁的写法
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L.append(0)
#         L = [L[i] + L[i-1] for i in range(len(L))] 
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 5:
#         break

# def normalize(name):
#     return name.capitalize()
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
from functools import reduce
# def prod(L):
#     return reduce(lambda x, y: x * y, L)
# print(prod(range(1, 3)))

# def str2float(s):
#     l = s.split('.')
#     def char2num(s):
#         d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         return d[s]
#     def int(x, y):
#         return x * 10 + y
#     return reduce(int, map(char2num, l[0])) + reduce(int, map(char2num, l[1])) / (10**len(l[1]))

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# def _not_divisible(n):
#     return lambda x: x % n > 0
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

def is_palindrome(n):
    res = True
    l = [n for n in str(n)]
    length = len(l)
    if length > 1:
        for i, value in enumerate(l):
            if i < length / 2:
                if l[i] != l[length - i - 1]:
                    res = False
                    break
    else:
        res = False
    return res
# def is_palindrome(value):
#     if isinstance(value,int):
#         return str(value)==str(value)[::-1]
#     else:
#         return value==value[::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))