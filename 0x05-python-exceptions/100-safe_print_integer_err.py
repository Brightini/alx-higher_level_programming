#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    prints an integer

    Args:
        value: value of integer to be printed

    Return:
        True if an integer is printed, otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
