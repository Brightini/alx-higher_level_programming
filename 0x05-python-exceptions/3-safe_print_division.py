#!/usr/bin/python3
def safe_print_division(a, b):
    """
    divides 2 integers and prints the result

    Args:
        a: first integer
        b: second integer

    Return:
        the result of dividing a by b or None if it fail
    """
    try:
        result = a / b
    except (ValueError, ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
