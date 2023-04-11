#!/usr/bin/python3
"""100-my_int module"""


class MyInt(int):
    """MyInt class"""
    def __init__(self, value):
        """Instantiates object"""
        self.value = value

    def __eq__(self, other):
        """inverts the == operation"""
        return self.value != other

    def __ne__(self, other):
        """inverts the != operation"""
        return self.value == other
