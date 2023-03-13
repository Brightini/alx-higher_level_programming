#!/usr/bin/python3
from sys import argv
sum = 0
count = len(argv)
for i in range(1, count):
    sum += int(argv[i])
print("{}".format(sum))
