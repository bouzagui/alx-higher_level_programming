#!/usr/bin/python3
""" convert student """


class Student:
    """ Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                reserved = {}
                for attr in attrs:
                    if attr in self.__dict__:
                        reserved[attr] = getattr(self, attr)
                return reserved
        return self.__dict__
