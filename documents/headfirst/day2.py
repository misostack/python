#!/usr/bin/env python3

"""Int"""
a = 1

print(type(a))

"""Float"""

b = 1.0

print(type(b))

"""Complex"""

c = 1+2j

print(type(c))

"""List"""

a_list = [1, 'a', 1.2, 1+2j]

print(a_list, a_list[0], a_list[0:3], a_list[:3], a_list[1:])

a_list[3] = 3

b_list = [3,4]

print(a_list)

"""Tuple"""

a_tuple = ("Apple", "Banana", "Orange")

print(a_tuple[0])

a_string = """
A multiline string
display here
"""

print(a_string)

set_a = {1,1,2,3}

set_b = {3,4,5}

print(set_a.union(set_b))

print(set_a.intersection({'b'}))

set_c = set_a.intersection({'b'})

print(set_c or False)

dic_a = {'first_name': 'Son', 'last_name': 'Nguyen'}

print(dic_a['first_name'], dic_a['last_name'])

print(dic_a.keys())


print(dict([['a',2], ['b',4]]))