#!/usr/bin/python3
""" that function to write a string to a file """


def write_file(filename="", text=""):
    """ write a string to a file """
    with open(filename, 'w', encoding='utf-8') as f:
        """ print format string """
        write_f = f.write(text)
        return write_f
