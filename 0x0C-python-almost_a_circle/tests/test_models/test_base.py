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

    def test_save_to_file_empty_list_for_Square(self):
        """ Test to save an empty list for Square object """
        Square.save_to_file(None)
        with open("Square.json", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_argument_None_for_Square(self):
        """ Test to save when argument is None for Square object"""
        Square.save_to_file([])
        with open("Square.json", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_empty_list_for_Rectangle(self):
        """ Test for save an empty list for Rectangle object """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_argument_None_for_Rectangle(self):
        """ Test to save when argument is None for Rectangle object """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_from_json_string_non_empty_list(self):
        """ Test for deserialization of non-empty list """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_empty_list(self):
        """ Test for deserialization of empty list """
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_None_argument(self):
        """ Test for deserialization when argument is None """
        json_list_input = Rectangle.to_json_string(None)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    # def test_create(self):
    #     """ Test for create method """
    #     r4 = Rectangle(3, 5, 1)
    #     r4_dictionary = r4.to_dictionary()
    #     r5 = Rectangle.create(**r4_dictionary)
    #     self.assertEqual(str(print(r4)), "[Rectangle] (5) 1/0 - 3/5")
    #     self.assertEqual(str(print(r5)), "[Rectangle] (5) 1/0 - 3/5")
    #     self.assertFalse(r4 is r5)
    #     self.assertFalse(r4 == r5)
