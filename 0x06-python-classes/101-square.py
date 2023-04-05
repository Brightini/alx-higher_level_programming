#!/usr/bin/python3
"""Square module"""


class Square():
    """A Square class"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square.

        Return:
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
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Get position of square object

        Return:
            position of square object
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set position of square object

        Args:
            value: (tuple) position of square object

        Raises:
            TypeError: if @value is not a tuple of integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Computes and returns the area of a Square object"""
        return self.__size ** 2

    def my_print(self):
        """
        prints a square using the '#' character
        """
        if self.__size <= 0:
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size, end="")
            # to not print newline after square is printed
            if _ < self.__size - 1:
                print()

    def __str__(self):
        """
        ensures that Square instance should
        have the same behavior as my_print()
        """
        self.my_print()
        return ""
