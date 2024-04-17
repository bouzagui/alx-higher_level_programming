#!/usr/bin/python3
""" definitions """


def class_to_json(obj):
    """ Convert a class to JSON
    """
    return obj.__dict__
