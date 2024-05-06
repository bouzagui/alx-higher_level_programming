#!/usr/bin/python3
''' class method '''
from models.base import Base


class Rectangle(Base):
    ''' Rectangle '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''get the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set width value'''
        self.__width = value

    @property
    def height(self):
        ''' get height '''
        return self.__height

    @height.setter
    def height(self, value):
        '''set height value'''
        self.__height = value

    @property
    def x(self):
        ''' get x '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' set x value '''
        self.__x = value

    @property
    def y(self):
        ''' get y '''
        return self.__y

    @y.setter
    def width(self, value):
        ''' set y value '''
        self.__y = value
