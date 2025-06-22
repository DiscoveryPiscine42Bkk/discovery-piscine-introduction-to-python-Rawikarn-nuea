#!/usr/bin/env python3
user_input_num = int(input( " Enter a number less than 25 "))
# var = input("prompt")

if user_input_num < 25 :
    count = user_input_num
    while count <= 25:
        print(f"Inside the loop, my variable is {count}")
        count += 1
else :
    print ("Erro