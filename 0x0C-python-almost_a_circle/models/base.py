#!/usr/bin/python3
"""Defines the Base class"""
import json


class Base:
    """A Base class"""
    __nd_objects = 0

    def __init__(self, id=None):
        """
        Instantiates an instance if Base class

        Args:
            id: id of Base class instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON representation

        Args:
            list_dictionaries: a list of dictionaries

        Return:
            JSON representation of @list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        json_rep = json.dumps(list_dictionaries)
        return json_rep

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save JSON representation of an object to a JSON file.

        First, it converts the list of object(@list_objs) to a
        list of the dictionary representation of objects. Then
        saves the result to a json file of this format:
        <Class name>.json

        Args:
            list_objs: a list of objects
        """
        dict_list = []
        for obj in list_objs:
            dict_list.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", "w", encoding="UTF-8") as file:
            json.dump(dict_list, file)

    def to_dictionary(self):
        """ Returns the dictionary representation of an object"""
        data = {}
        # iterate over all attributes of the object
        for attr in self.__dict__:
            # to remove class name and '_' prefix of attribute name
            key = attr.lstrip('_').split('_')[-1]
            # get the value of the attribute
            value = getattr(self, attr)
            # collect data for serializable attributes
            data[key] = value
        return data
