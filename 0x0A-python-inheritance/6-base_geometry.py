#!/usr/bin/python3
""" this function is used to generate the output """


class BaseGeometry:
    """ Base class for Geometry """
    def area(self):
        raise Exception("area() is not implemented")
