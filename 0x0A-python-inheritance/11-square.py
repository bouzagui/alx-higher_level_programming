#!/usr/bin/python3
""" defined a class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ method """
        return self.__size * self.__size

    def __str__(self):
        """ method """
        return "[Square] {}/{}".format(self.__size, self.__size)
