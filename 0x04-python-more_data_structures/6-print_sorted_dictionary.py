#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = ["Number", "ids", "language", "track"]
    for i in keys:
        if i in a_dictionary:
            print("{}: {}".format(i, a_dictionary[i]))