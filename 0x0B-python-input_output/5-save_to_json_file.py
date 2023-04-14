#!/usr/bin/python3
"""Defines save_to_json_file() function"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serializes a python object and saves it to a file

    Args:
        my_obj: python object
        filename: file to which JSON string rep is to be written
    """
    with open(filename, 'w', encoding="UTF-8") as j_file:
        json.dump(my_obj, j_file)
