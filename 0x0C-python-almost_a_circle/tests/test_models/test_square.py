"""Defines test cases for Square class"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """ Test for Square class """

    @classmethod
    def setUpClass(cls):
        """ Set up class instances """
        cls.s1 = Square(5)
        cls.s2 = Square(2, 2)
        cls.s3 = Square(3, 1, 3)
        cls.s4 = Square(5)

    def test_object_id(self):
        """ Test for instance id """
        self.assertEqual(self.s1.id, 8)
        self.assertEqual(self.s2.id, 9)
        self.assertEqual(self.s3.id, 10)

    def test_size_setter(self):
        """ Test for size setter method """
        self.s1.size = 10
        self.assertEqual(str(self.s1), "[Square] (8) 0/0 - 10")

        with self.assertRaises(TypeError):
            self.s1.size = "h"

    def test_str_method(self):
        """ Test for __str__ method """
        self.assertEqual(str(self.s1), "[Square] (8) 0/0 - 10")
        self.assertEqual(str(self.s2), "[Square] (9) 2/0 - 2")
        self.assertEqual(str(self.s3), "[Square] (10) 1/3 - 3")

    def test_area(self):
        """ Test for area """
        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 9)

    def test_update_method_for_args(self):
        """ Test for update method for args """
        self.s4.update(10)
        self.assertEqual(str(self.s4), "[Square] (10) 0/0 - 5")
        self.s4.update(1, 2)
        self.assertEqual(str(self.s4), "[Square] (1) 0/0 - 2")
        self.s4.update(1, 2, 3)
        self.assertEqual(str(self.s4), "[Square] (1) 3/0 - 2")
        self.s4.update(1, 2, 3, 4)
        self.assertEqual(str(self.s4), "[Square] (1) 3/4 - 2")

    def test_update_method_for_kwargs(self):
        """ Test for update method for kwargs """
        self.s4.update(x=12)
        self.assertEqual(str(self.s4), "[Square] (1) 12/4 - 2")
        self.s4.update(size=7, y=1)
        self.assertEqual(str(self.s4), "[Square] (1) 12/1 - 7")
        self.s4.update(size=7, id=89, y=1)
        self.assertEqual(str(self.s4), "[Square] (89) 12/1 - 7")