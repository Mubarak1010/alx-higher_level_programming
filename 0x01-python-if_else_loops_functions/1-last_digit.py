#!/usr/bin/python3
import random
number = random.randint(-10000, 0)
num = abs(number) % 10
if number < 0:
    num = -num
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
if num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
elif num == 0:
    print(f"Last digit of {number} is {num} and is 0")
elif num < 6:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
