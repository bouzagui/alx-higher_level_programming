#!/usr/bin/python3
""" Defines a square """


class Square:
    """ This class defines a square """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
