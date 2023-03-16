#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    replaces or adds key/value in a dictionary

    Args:
        key: unique value identifier
        value: value pointed to be key
    
    Return:
        updated dictionary    
    """
    a_dictionary[key] = value
    return a_dictionary
