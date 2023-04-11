#!/usr/bin/python3
"""101-add_attribute module"""


def add_attribute(obj, attr, value):
    """
    adds attribute to an object if it is possible

    Args:
        obj: object to receive new attributes
        attr: attribute name
        value: attribute value

    Raise(s):
        TypeError: if new attribute can't be added
    """
    # to check if obj is an instance if a user-defined class or
    # is an instances of built-in types that allow dynamic attribute creation
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr] = value
    # if not, exception is raised
    else:
        raise TypeError("can't add new attribute")
