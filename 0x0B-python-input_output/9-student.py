#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        data = {}

        # iterate over all attributes of the object
        for attr in self.__dict__:
            # get the value of the attribute
            value = getattr(self, attr)
            # collect data for serializable attributes
            if isinstance(value, (list, dict, str, int, bool)):
                data[attr] = value
        return data
