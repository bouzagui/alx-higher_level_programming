#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    @property
    def size(self):
        return self.__size
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value
    def area(self):
        return self.__size * self.__size
