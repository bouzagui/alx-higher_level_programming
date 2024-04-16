#!/usr/bin/python3
""" defined a function that returns a string """


def is_kind_of_class(obj, a_class):
    """ returns true if the class is a kind of class """
    try:
        if isinstance(obj, a_class):
            return True
        elif not isinstance(obj, a_class):
            return False
    except TypeError:
        pass
