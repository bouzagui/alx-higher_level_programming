#!/usr/bin/python3
""" modules """
import json


class Base:
    """ Base class for all modules """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        elif id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
