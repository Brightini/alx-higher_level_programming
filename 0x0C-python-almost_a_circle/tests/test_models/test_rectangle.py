""" Defines test cases for Rectangle class """
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ Test cases for rectangle class """

    @classmethod
    def setUpClass(cls):
        """ Set up class instances """
        cls.r1 = Rectangle(1, 2)
        cls.r2 = Rectangle(1, 2, 3)
        cls.r3 = Rectangle(1, 2, 3, 4)
        cls.r4 = Rectangle(1, 2, 3, 4, 15)
        cls.r10 = Rectangle(10, 10, 10, 10)
        cls.r11 = Rectangle(10, 10, 10, 10)
        cls.r12 = Rectangle(10, 2, 1, 9)
        cls.r13 = Rectangle(1, 1)

    def test_object_id(self):
        """ Test for instance id """
        self.assertEqual(self.r1.id, 16)
        self.assertEqual(self.r2.id, 17)
        self.assertEqual(self.r3.id, 18)
        self.assertEqual(self.r4.id, 15)

    def test_width_setter(self):
        """ Test width setter """
        self.r4.width = 10
        self.assertEqual(self.r4.width, 10)

    def test_height_setter(self):
        """ Test height getter """
        self.r4.height = 7
        self.assertEqual(self.r4.height, 7)

    def test_x_setter(self):
        """ Test x getter """
        self.r4.x = 9
        self.assertEqual(self.r4.x, 9)

    def test_y_setter(self):
        """ Test y getter """
        self.r4.y = 7
        self.assertEqual(self.r4.y, 7)

    def test_attribute_error(self):
        """ Test for errors in instance attributes """
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
        """ Test for area """
        self.assertEqual(self.r1.area(), 2)
        self.assertEqual(self.r4.area(), 2)

    def test_str_method(self):
        """ Test for __str__ method """
        self.assertEqual(str(self.r3), "[Rectangle] (18) 3/4 - 1/2")
        self.assertEqual(str(self.r4), "[Rectangle] (15) 3/4 - 1/7")

    def test_update_method_for_args(self):
        """ Test for update method for args """
        self.assertEqual(str(self.r10), "[Rectangle] (19) 10/10 - 10/10")
        self.r10.update(89)
        self.assertEqual(str(self.r10), "[Rectangle] (89) 10/10 - 10/10")
        self.r10.update(89, 2)
        self.assertEqual(str(self.r10), "[Rectangle] (89) 10/10 - 2/10")
        self.r10.update(89, 2, 3)
        self.assertEqual(str(self.r10), "[Rectangle] (89) 10/10 - 2/3")
        self.r10.update(89, 2, 3, 4)
        self.assertEqual(str(self.r10), "[Rectangle] (89) 4/10 - 2/3")
        self.r10.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.r10), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_method_for_kwargs(self):
        """ Test for update method for kwargs """
        self.r11.update(200, height=1)
        self.assertEqual(str(self.r11), "[Rectangle] (200) 10/10 - 10/10")
        self.r11.update(height=1)
        self.assertEqual(str(self.r11), "[Rectangle] (200) 10/10 - 10/1")
        self.r11.update(width=1, x=2)
        self.assertEqual(str(self.r11), "[Rectangle] (200) 2/10 - 1/1")
        self.r11.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(self.r11), "[Rectangle] (89) 3/1 - 2/1")
        self.r11.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(self.r11), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        """ Test for dictionary represention of object """
        r12_dictionary = self.r12.to_dictionary()
        self.assertEqual(str(type(r12_dictionary)), "<class 'dict'>")
        self.r13.update(**r12_dictionary)
        self.assertFalse(self.r12 == self.r13)
