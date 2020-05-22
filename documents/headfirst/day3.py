#/usr/bin/env
import math

num_int = 123
num_flo = 123.123

print('PI = {}'.format(math.pi))

num_new = num_int + num_flo

print(num_new)

num_str = "456"

num_sum = num_int + int(num_str)

print(num_sum)

print(1,2,3, sep='*', end="\t")
print('=', 1+2+3)

print('I love {0} and {1}'.format('bread','butter'))

print('My name is {first_name} {last_name}'.format(first_name = 'Son', last_name = 'Nguyen'))

print('The new number is %3.2f' % num_new)

num = input('Enter a number:')

print(int(num))