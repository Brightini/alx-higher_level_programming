#!/usr/bin/python3
"""Defines the Base class"""
import json
import os


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
        json_rep = json.dumps(list_dictionaries, ensure_ascii=False)
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
        if list_objs:
            # convert to list of dictionaries
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
            # get JSON representation of @dict_list
            json_rep = cls.to_json_string(dict_list)
            # write to json file
            with open(f"{cls.__name__}.json", "w", encoding="UTF-8") as file:
                file.write(json_rep)
        else:
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

    @staticmethod
    def from_json_string(json_string):
        """
        Deserializes the JSON string @json_string

        Args:
            json_string: JSON string representation

        Return:
            the list of the JSON string representation @json_string
        """
        empty_list = []
        if not json_string:
            return empty_list
        else:
            json_rep = json.loads(json_string)
            return json_rep

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set

        Args:
            dictionary: contains attributes and their data

        Return:
            instance with all attributes already set
        """
        dummy_instance = cls(7, 2, 3)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Loads data from a .json file and returns a list of instances

        Return:
            a list of instances
        """
        list_of_instances = []

        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return list_of_instances
        else:
            # open file and load json data
            with open(filename, "r", encoding="UTF-8") as file:
                json_data = json.load(file)

            # convert data to json string
            json_string = json.dumps(json_data)

            # convert to list of deserialized json string
            list_of_json_rep = cls.from_json_string(json_string)
            for attr in list_of_json_rep:
                list_of_instances.append(cls.create(**attr))
            return list_of_instances

    def update(self, *args, **kwargs):
        """
        Updates object attributes

        Args:
            args: arguments for values of class attributes
            kwargs: dictionary containing attributes and their values
        """
        attr = ['id', 'width', 'height', 'x', 'y']
        if len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save JSON representation of an object to a .csv file.

        First, it converts the list of object(@list_objs) to a
        list of the dictionary representation of objects. Then
        saves the result to a .csv file of this format:
        <Class name>.csv

        Args:
            list_objs: a list of objects
        """
        dict_list = []
        if list_objs:
            # convert to list of dictionaries
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
            # get JSON representation of @dict_list
            json_rep = cls.to_json_string(dict_list)
            # write to .csv file
            with open(f"{cls.__name__}.csv", "w", encoding="UTF-8") as file:
                file.write(json_rep)
        else:
            with open(f"{cls.__name__}.csv", "w", encoding="UTF-8") as file:
                json.dump(dict_list, file)

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads data from a .csv file and returns a list of instances

        Return:
            a list of instances
        """
        list_of_instances = []

        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return list_of_instances
        else:
            # open file and load json data
            with open(filename, "r", encoding="UTF-8") as file:
                json_data = json.load(file)

            # convert data to json string
            json_string = json.dumps(json_data)

            # convert to list of deserialized json string
            list_of_json_rep = cls.from_json_string(json_string)
            for attr in list_of_json_rep:
                list_of_instances.append(cls.create(**attr))
            return list_of_instances
