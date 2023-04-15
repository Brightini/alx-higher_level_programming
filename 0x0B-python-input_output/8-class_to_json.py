#!/usr/bin/python3
"""Defines save_to_json_file() function"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    data = {}

    # iterate over all attributes of the object
    for attr in obj.__dict__:
        # get the value of the attribute
        value = getattr(obj, attr)
        # collect data for serializable attributes
        if isinstance(value, (list, dict, str, int, bool)):
            data[attr] = value
    return data
