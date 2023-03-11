#!/usr/bin/python3
def uppercase(str):
    """coverts lowercase to uppercase character"""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = ord(char) - 32
            print("{}".format(chr(char)), end="")
        else:
            print("{}".format(char), end="")
    print()
