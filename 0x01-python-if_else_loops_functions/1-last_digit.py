#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if number < 0:
    num = -num
    if num = 0:

    print(f"Last digit of {number} is {num} and is is less than 6 and not 0")
elif num == 0:
    print(f"Last digit of {number} is {num} and is 0")
elif num < 6 and num != 0:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
