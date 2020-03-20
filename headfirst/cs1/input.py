#!/usr/bin/env python3
import sys, getopt

print("1.Input\n")

# print(sys.argv)
try:
  opts, args = getopt.getopt(sys.argv[1:],"i:o",["input=", "output="])
  print(opts)
except getopt.GetoptError:
  sys.exit(2)