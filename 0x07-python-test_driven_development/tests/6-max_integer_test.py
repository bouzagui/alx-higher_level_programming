#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
def max_integer(list=[]):
    if len(list) == 0:
        return None
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
