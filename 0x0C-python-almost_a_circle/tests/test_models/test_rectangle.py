"""Defines test cases for Rectangle class"""
import unittest
import doctest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test cases for rectangle class"""

    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(1, 2)
        cls.r2 = Rectangle(1, 2, 3)
        cls.r3 = Rectangle(1, 2, 3, 4)
        cls.r4 = Rectangle(1, 2, 3, 4, 15)

    def test_id_passed(self):
        self.assertEqual(self.r1.id, 3)
        self.assertEqual(self.r2.id, 4)
        self.assertEqual(self.r3.id, 5)
        self.assertEqual(self.r4.id, 15)

    def test_width_setter(self):
        """Test width setter"""
        self.r4.width = 10
        self.assertEqual(self.r4.width, 10)

    def test_height_getter(self):
        """Test height getter"""
        self.r4.height = 7
        self.assertEqual(self.r4.height, 7)

    def test_x_getter(self):
        """Test x getter"""
        self.r4.x = 9
        self.assertEqual(self.r4.x, 9)

    def test_y_getter(self):
        """Test y getter"""
        self.r4.y = 7
        self.assertEqual(self.r4.y, 7)

    def test_attribute_error(self):
        """Test for errors in instance attributes"""
        with self.assertRaises(TypeError):
            Rectangle(1, "h")
            Rectangle(6.98, 4)
        with self.assertRaises(ValueError):
            Rectangle(0, 6)
            Rectangle(-1, 7)
            Rectangle(5, -3)
            Rectangle(8, 0)
            Rectangle(2, 1, -7, 9)
            Rectangle(5, 9, 2, -10)

    def test_area(self):
        """Test for area"""
        self.assertEqual(self.r1.area(), 2)
        self.assertEqual(self.r4.area(), 2)

    def test_str_method(self):
        """Test for __str__ method"""
        self.assertEqual(str(self.r3), "[Rectangle] (5) 3/4 - 1/2")
        self.assertEqual(str(self.r4), "[Rectangle] (15) 3/4 - 1/7")
