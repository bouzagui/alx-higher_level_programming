#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for i in sorted_keys:
        if i in a_dictionary:
            print("{}: {}".format(i, a_dictionary[i]))
