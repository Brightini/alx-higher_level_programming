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
        self.__size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The value of the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size of a Square object

        Args:
            size: (int) new value for the size attribute

        Raises:
            TypeError: if @size is not an int
            ValueError: if @size is less than 0
        """
        if isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes and returns the area of a Square object"""
        return self.__size ** 2

    def __eq__(self, other) -> bool:
        """checks if object areas are equal"""
        return self.area() == other.area()

    def __ne__(self, other) -> bool:
        """checks if object areas are not equal"""
        return self.area() != other.area()

    def __gt__(self, other) -> bool:
        """checks if one object area is greater than another"""
        return self.area() > other.area()

    def __ge__(self, other) -> bool:
        """checks if one object area is greater than or equal to another"""
        return self.area() >= other.area()

    def __lt__(self, other) -> bool:
        """checks if one object area is less than another"""
        return self.area() < other.area()

    def __le__(self, other) -> bool:
        """checks if one object area is less than or equal to another"""
        return self.area() <= other.area()
