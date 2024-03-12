#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

if number < 6:
    print(f"Last digit of {number:d} is 5 and is less than 6 and not 0")
elif number > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is greater than")
else:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
