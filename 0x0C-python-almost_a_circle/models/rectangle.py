#!/usr/bin/python3
""" module for creating and updating objects from different sources """
from models.base import Base


class Rectangle(Base):
    """
    arguments for creating and updating objects from different sources
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ returns the width of attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """ documents attribute """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ returns the height of attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ documents attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ returns the x coordinate """
        return self.__x

    @x.setter
    def x(self, value):
        """ documents attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ returns the y coordinate """
        return self.__y

    @y.setter
    def y(self, value):
        """ documents attribute """
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height
