#!/usr/bin/python3


def uppercase(str):
    for ch in str:
        if ord(ch) >= 'a' and ord(ch) <= 'z':
            ch = chr(ord(ch) - 32)
        else:
            print("{:s}".format(ch), end="")
    print()
