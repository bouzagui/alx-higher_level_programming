#!/usr/bin/python3
''' class method '''
from models.base import Base


class Rectangle(Base):
    ''' Rectangle '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''get the width'''
        return self.width

    @width.setter
    def width(self, value):
        '''set width value'''
        self.width = value

    @property
    def height(self):
        ''' get height '''
        return self.height

    @height.setter
    def height(self, value):
        '''set height value'''
        self.height = value

    @property
    def x(self):
        ''' get x '''
        return self.x

    @x.setter
    def x(self, value):
        ''' set x value '''
        self.x = value

    @property
    def y(self):
        ''' get y '''
        return self.y

    @y.setter
    def width(self, value):
        ''' set y value '''
        self.y = value
