#!/usr/bin/python3
"""Adds arguments to a python list"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# create empty list
my_list = []

# get arguments from command line
arguments = sys.argv[1:]

# checks if json file exists
# if it does the a python object is returned
if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")

# append new argumnts
my_list.extend(arguments)

# finally serialize python object
save_to_json_file(my_list, "add_item.json")
