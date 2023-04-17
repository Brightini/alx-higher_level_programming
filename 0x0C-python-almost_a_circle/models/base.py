#!/usr/bin/python3
"""Defines the Base class"""


class Base:
    """A Base class"""
    __nd_objects = 0

    def __init__(self, id=None):
        """
        Instantiates an instance if Base class

        Args:
            id: id of Base class instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects
