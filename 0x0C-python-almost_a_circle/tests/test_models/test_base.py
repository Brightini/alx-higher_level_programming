"""Defines test cases for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBaseClass(unittest.TestCase):
    """ Test cases for Base class """

    def test_id_passed(self):
        """ Test for id passed as argument """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_id_not_passed(self):
        """ Test for no argument """
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_private_class_instance(self):
        """ Test to access private class instance """
        b3 = Base()
        with self.assertRaises(AttributeError):
            print(b3.__nd_objects)

    def test_to_json_rep_method(self):
        """ Test for json representation """
        r1 = Rectangle(10, 7, 2, 8)
        # to convert to regular object dictionary
        dictionary = r1.to_dictionary()
        self.assertEqual(str(type(dictionary)), "<class 'dict'>")
        # to convert to json represention
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str(type(json_dictionary)), "<class 'str'>")
        # when parameter is empty or None
        empty_dictionary = Base.to_json_string(None)
        self.assertEqual(str(empty_dictionary), "[]")

    def test_save_to_file(self):
        """ Test to save to a json file """
        # first for Rectangle class
        r2 = Rectangle(13, 3, 1, 0)
        r3 = Rectangle(10, 8)
        Rectangle.save_to_file([r2, r3])
        with open("Rectangle.json", "r", encoding="UTF-8") as r_file:
            r_file.read()
        self.assertTrue(os.path.exists("Rectangle.json"))
        # next for Square class
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Square.json"))
