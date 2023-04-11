#!/usr/bin/python3
"""3-is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """
    checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class

    Args:
        obj: object ot be checked
        a_class: type of class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
