#!/usr/bin/python3
"""Defines a append_write() method"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file

    Args:
        filename: name of file
        text: string to be appended

    Return:
        number of characters appended
    """
    with open(filename, 'a', encoding="UTF-8") as a_file:
        n_char = a_file.write(text)
    return n_char
