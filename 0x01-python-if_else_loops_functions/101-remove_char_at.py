#!/usr/bin/python3
def remove_char_at(str, n):
    """removing the character at the position n"""
    if n < 0:
        return
    return str[:n] + str[n+1:]
