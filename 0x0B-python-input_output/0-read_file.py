#!/usr/bin/python3
""" that function to read file """


def read_file(filename=""):
    """ read file """
    with open(filename, "r", encoding='utf-8') as format:
        """ print format string """
        print(format.read(), end="")
