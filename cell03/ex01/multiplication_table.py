#!/usr/bin/env python3
number = int(input("Enter a number to display its multiplication table: "))

print(f"\nMultiplication Table for {number}:\n")
for i in range(1, 13):
    result = number * i
    print(f"{number} x {i} = {result}")