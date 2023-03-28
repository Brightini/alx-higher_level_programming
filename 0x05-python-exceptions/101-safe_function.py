#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    executes a function safely

    Args:
        fct: function to be executed
        args: arbitrary argument lists

    Return:
        result of function executed, otherwise None
    """
    try:
        return fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
