#!/usr/bin/env python3
num1 = int(input())
num2 = int(input())
product = num1 * num2

print(f"{product}")

if product == 0:
      print("The result is zero")

elif product > 0:
    print("The result is positive")

else:
    print("The result is negative")
