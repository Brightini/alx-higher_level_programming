#!/usr/bin/python3
"""4-inherits_from module"""


def inherits_from(obj, a_class):
    """
    checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj: object ot be checked
        a_class: type of class
    """
    # issubclass, to check if obj is a subclass of a_class
    # the other part of the condition, to ensure obj...
    # ...is not an instance of a_class
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
