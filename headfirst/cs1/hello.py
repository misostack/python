#!/usr/bin/env python3

import getopt, sys

def main():
  try:
    opts, args = getopt.getopt(sys.argv[1:], "hf:l:v", ["help","firstname=","lastname="])  
  except getopt.GetoptError as err:
    assert False, err
    sys.exit(2)

  fullname = None
  verbose = False
  for k, v in opts:
    if k in ('--help', '-h'):
      print(' \
      hello.py -v --firstname="Son" --lastname="Nguyen Minh" \
      ')
      sys.exit(2)      
    if k == '-v':
      verbose = True
    if k in ("--firstname", "-f"):
      fullname = v
    if k in ("--lastname", "-l"):
      fullname += " {}".format(v)

  if verbose:
    print(opts)
    print(args)

  if fullname:
    print("Hello, %s" %fullname)

if __name__ == "__main__":
  main()