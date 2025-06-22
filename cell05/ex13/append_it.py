#!/usr/bin/env python3
import sys

args = sys.argv[1:]
printed = False

for word in args:
    if not word.endswith("ism"):
        print(f"{word}ism$")
        printed = True

if not args or not printed:
    print("none")