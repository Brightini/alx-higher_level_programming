#!/usr/bin/python3
"""7-base_geometry module"""


class BaseGeometry:
    """A BaseGeometry class"""
    def area(self):
        """a public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates a value

        Args:
            name: attribute name
            value: attribute value

        Raise(s):
            TypeError: if @value is not an int
            ValueError: if @value is <= 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
