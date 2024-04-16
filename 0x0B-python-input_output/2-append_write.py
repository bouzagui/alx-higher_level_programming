#!/usr/bin/python3
""" append a string """


def append_write(filename="", text=""):
    """ append a string """
    with open(filename, 'a', encoding='utf-8') as f:
        """ append a string """
        append_w = f.write(text)
        return append_w
