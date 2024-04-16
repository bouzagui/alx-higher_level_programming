#!/usr/bin/python3
""" defined a function that returns a string """


def inherits_from(obj, a_class):
    """ returns True if obj is a class of a given class """
    return isinstance(obj, a_class) and not type(obj) is a_class
