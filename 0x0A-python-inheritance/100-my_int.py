#!/usr/bin/python3
""" Class MyInt inherits from int with inverted == and != operators. """


class MyInt(int):
    """ class MyInt """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)