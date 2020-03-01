#!/usr/bin/env python3

print("0.Implicit casting type\n")
x = 1
print("The type of {} is {}".format(x, type(x)))
x = 1.2
print("The type of {} is {}".format(x, type(x)))
x = '1'
print("The type of '{}' is {}".format(x, type(x)))
x = False
print("The type of {} is {}".format(x, type(x)))
x = None
print("The type of {} is {}".format(x, type(x)))
x = 'False'
print("The type of '{}' is {}".format(x, type(x)))

print("1. Sum of a list of numbers from input\n")

numbers = input("Please enter a list of number:")
total = 0
print("-"*20)
print("Sum of \"{}\" is \"{}\"\n".format(numbers, total))
