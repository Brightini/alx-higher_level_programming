#!/usr/bin/python3
"""2-is_same_class module"""


def is_same_class(obj, a_class):
    """
    checks whether object is exactly an instance of the specified class

    Args:
        obj: object ot be checked
        a_class: type of class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
