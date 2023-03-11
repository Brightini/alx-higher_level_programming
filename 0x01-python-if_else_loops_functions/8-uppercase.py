#!/usr/bin/python3
def uppercase(str):
    """coverts lowercase to uppercase character"""
    result = ""  # To store characters (included those converted)
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        result += char
    print("{}".format(result))
