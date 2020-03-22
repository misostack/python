#!/usr/bin/env python3
# import sys, getopt

# print("1.Input\n")

# try:
#   opts, args = getopt.getopt(sys.argv[1:],"i:o",["input=", "output="])
#   print(opts)
# except getopt.GetoptError:
#   sys.exit(2)

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))