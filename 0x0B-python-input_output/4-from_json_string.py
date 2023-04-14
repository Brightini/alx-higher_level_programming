#!/usr/bin/python3
"""Defines from_json_string() function"""
import json


def from_json_string(my_str):
    """
    Deserializes a json string to a python object

    Args:
        my_str: variable holding json string

    Return:
        python object
    """
    p_obj = json.loads(my_str)
    return p_obj
