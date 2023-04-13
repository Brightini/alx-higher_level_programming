#!/usr/bin/python3
"""Defines to_json_string() function"""
import json


def to_json_string(my_obj):
    """
    serializes an object

    Args:
        my_obj: object to be serialized

    Return:
        a json representation of @my_obj
    """
    j_rep = json.dumps(my_obj)
    return j_rep
