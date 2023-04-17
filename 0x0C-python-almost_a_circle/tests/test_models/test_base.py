import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    def test_id(self):
        """test instance id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        