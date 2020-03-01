#!/usr/bin/env python3

print("Sequence Types\n")

aString = "This is headfirst series of python."

aList = [0, -1, 1, "2", "3", "four", "five", 6.0, 7.0, 8.0, 9.0, 0.1*100]

print("Type of {} is {}".format(aList, type(aList)))

aTuple = (0, "a", None, False, True, 1j, 0.2, "red", "green", "blue")

print("Type of {} is {}".format(aTuple, type(aTuple)))

aRange = range(2, 10) # if you don't set the start of the range, by default it will start from 0

print("Type of {} is {}".format(aRange, type(aRange)))

anEmptyTuple = ()
anEmptyList = []
anEmptyRange = range(0)

print("Is {} is truthy? {}".format(anEmptyTuple, bool(anEmptyTuple)))

print("Is {} is truthy? {}".format(anEmptyList, bool(anEmptyList)))

print("Is {} is truthy? {}".format(anEmptyRange, bool(anEmptyRange)))
