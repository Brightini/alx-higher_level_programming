#!/usr/bin/python3
"""Square module"""


class Square():
    """A Square class"""
    def __init__(self, size=0):
        """Iniatializes an instance attribute(s)"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
