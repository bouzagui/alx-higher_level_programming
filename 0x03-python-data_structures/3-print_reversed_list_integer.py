#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = my_list[::-1]
    idx = 0
    while idx < len(reversed_list):
        print("{:d}".format(reversed_list[idx]))
        idx += 1
