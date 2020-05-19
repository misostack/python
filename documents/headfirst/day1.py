#!/usr/bin/env python3
import constant

print("First day to learn python3")

print("First day to learn python3 2")

print(False, True, None)

x = 1 + 2 + 3 + 4 + 5 + 6

print(x)

x = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

print(x)

a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)

print(a)

colors = ['green',
          'blue',
          'red']

print(colors)

a = 1; b = 2; c = 3

print(a, b, c)

for i in range(1, 12):
    print(i)
    if i == 5:
        break

if True:
    print('Hello')
    a = 5

if True: print('Hello'); a = 5

def square(n):
    '''Takes in a number n, return the square of n'''
    return n**2

print(square.__doc__)

a, b, c = 3, 2, "add"

print(a, b, c)

x = y = z = 1

print(x, y, z)

print(constant.PI, constant.GRAVITY)
