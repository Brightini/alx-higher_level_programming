#!/usr/bin/python3
""" Defines Rectangle class """
from models.base import Base


class Rectangle(Base):
    """A Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiates Rectangle instances

        Args:
            width: (int) width of Rectangle object
            height: (int) height of Rectangle object
            x: (int)
            y: (int)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """ Returns string representation of Rectangle instance """
        str_rep = "[{}] ({}) {}/{} - {}/{}"
        idd, xx, yy, w = self.id, self.__x, self.__y, self.__width
        h = self.__height
        return str_rep.format(__class__.__name__, idd, xx, yy, w, h)

    @property
    def width(self):
        """Gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width

        Args:
            value: (int) value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Gets height """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height

        Args:
            value: (int) value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gets x """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets x

        Args:
            value: (int) value of x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets y """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets y

        Args:
            value: (int) value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Computes and returns the area of a Rectangle object """
        return (self.__width * self.__height)

    def display(self):
        """ Prints Rectangle instance with character '#' """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x, end="")
            for _ in range(self.__width):
                print('#', end="")
            print()

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

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle object"""
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
