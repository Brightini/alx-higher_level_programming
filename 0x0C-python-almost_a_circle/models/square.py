#!/usr/bin/python3
""" Defines a Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiates Square instances

        Args:
            size: (int) size of Square object
            x: (int)
            y: (int)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """
        Returns string representation of Rectangle instance

        Note that width and height are equal for a Square object
        """
        str_rep = "[{}] ({}) {}/{} - {}"
        idd, xx, yy, w = self.id, self.x, self.y, self.width
        return str_rep.format(__class__.__name__, idd, xx, yy, w)

    @property
    def size(self):
        """ Returns object width """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets object's width

        Args:
            value: (int) value of object's width
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates object attributes

        Args:
            args: arguments for values of class attributes
        """
        attr = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle object"""
        data = {}
        # iterate over all attributes of the object
        for attr in self.__dict__:
            # to remove class name and '_' prefix of attribute name
            key = attr.lstrip('_').split('_')[-1]

            # use 'size' instead of 'width' or 'height'
            if key == 'width' or key == 'height':
                key = 'size'

            # get the value of the attribute
            value = getattr(self, attr)
            # collect data for serializable attributes
            data[key] = value
        return data
