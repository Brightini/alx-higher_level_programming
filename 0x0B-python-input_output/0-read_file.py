#!/usr/bin/python3
"""Defines a read_file() method"""


def read_file(filename=""):
    """
    Reads a text file and prints its content to stdout

    Args:
        filename: name of text file
    """
    with open(filename, "r", encoding="UTF-8") as a_file:
        text = a_file.read()
        print(text, end="")
