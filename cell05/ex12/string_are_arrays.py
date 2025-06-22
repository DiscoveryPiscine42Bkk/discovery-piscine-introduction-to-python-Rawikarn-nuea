#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if len(args) != 1:
    print("none")
else:
    count = 0
    for char in args[0]:
        if char == 'z':
            print('z', end='')
            count += 1
    if count == 0:
        print("none")
    else:
        print()