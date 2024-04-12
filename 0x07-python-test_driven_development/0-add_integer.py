#!/usr/bin/python3
def add_integer(a, b=98):
    """Function that adds 2 integers
    Args:
        a: first integer
        b: second integer
        return: the addition of a and b
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    return a + b
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
