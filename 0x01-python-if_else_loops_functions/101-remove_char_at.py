#!/usr/bin/python3
def remove_char_at(str, n):
    """removing the character at the position n"""
    return str[:n] + str[n+1:]
