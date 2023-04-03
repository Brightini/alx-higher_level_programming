#!/usr/bin/python3
"""Square module"""


class Square():
    """A Square class"""

    def __init__(self, size=0):
        """
        initializes the attributes of a Square instance

        Args:
            size: (int) value of size attribute
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The value of the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        set the size of a Square object

        Args:
            size: (int) new value for the size attribute

        Raises:
            TypeError: if @size is not an int
            ValueError: if @size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Computes and returns the area of a Square object"""
        return self.__size ** 2
