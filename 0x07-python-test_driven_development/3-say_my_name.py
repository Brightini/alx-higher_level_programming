#!/usr/bin/python3
"""3-say_my_name module"""


def say_my_name(first_name="", last_name=""):
    """
    prints first and last name

    Args:
        first_name: (str) first name of object
        last_name: (str): last name of object

    Raises:
        TypeError: if either @first_name or @last_name is not a string
    """
    if not isinstance(first_name, str) or not first_name:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
