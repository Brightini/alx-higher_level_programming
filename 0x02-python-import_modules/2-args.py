#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    # -1 to exclude the name of script
    count = len(argv)
    if count == 1:
        print("{} arguments.".format(count - 1))
    elif count == 2:
        print("{} argument:".format(count - 1))
    else:
        print("{} arguments:".format(count - 1))
    for i in range(1, count):
        print("{}: {}".format(i, argv[i]))
