#!/usr/bin/python3
""" Defines a square class """


class Square:
    """ Defines a square """
    def __init__(self, size=0):
        if size != int(size) or size < 0:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
