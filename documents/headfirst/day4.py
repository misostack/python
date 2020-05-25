#!/usr/bin/env python3

"""Falsy"""
data = [0, 0.1, "0", 1, True, False, [], (), {}]


for v in data:
  if v:
    print("{} with type= {} is TRUE".format(v, type(v)))
  else:
    print("{} with type= {} is FALSE".format(v, type(v)))

