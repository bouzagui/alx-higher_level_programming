#!/usr/bin/python3
""" defined a function that returns a string """


def is_same_class(obj, a_class):
    """ returns True if obj is a class of a given class """

    return type(obj).__name__ == a_class.__name__
