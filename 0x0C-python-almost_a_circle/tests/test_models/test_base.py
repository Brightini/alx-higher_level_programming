"""Defines test cases for Base class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test cases for Base class"""
    def test_id_passed(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_id_not_passed(self):
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_private_class_instance(self):
        b3 = Base()
        with self.assertRaises(AttributeError):
            print(b3.__nd_objects)
