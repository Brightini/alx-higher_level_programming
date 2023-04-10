#!/usr/bin/python3
"""add_integer module"""


def add_integer(a, b=98):
    """"
    computes the sum of two numbers

    Args:
        a: (int) first number
        b: (int) second number
        floats are casted to integers

    Raises:
        TypeError: of a or b is not an integer or float

    Return:
        sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    result = a + b
    if result == float('inf') or result == float('-inf'):
        raise OverflowError("float overflow")
    return int(a) + int(b)


if __name__ == '__main__':
    import doctest
    doctest.testfile('0-add_integer.txt')
