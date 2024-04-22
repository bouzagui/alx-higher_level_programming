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
        """ doct """
        self.__width = value

    @property
    def height(self):
        """ returns the height of attribute"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """ doct """
        self.__height = value
    
    @property
    def x(self):
        """ returns the x of attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """ doct """
        self.__x = value

    @property
    def y(self):
        """ returns the y of attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """ doct """
        self.__y = value
