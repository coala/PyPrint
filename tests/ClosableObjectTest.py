import unittest

from pyprint.ClosableObject import ClosableObject, close_objects


class ClosableObjectTest(unittest.TestCase):

    def setUp(self):
        self.uut = ClosableObject()

    def test_closing(self):
        self.assertFalse(self.uut._closed)
        self.uut.close()
        self.assertTrue(self.uut._closed)
        self.uut.close()
        self.assertTrue(self.uut._closed)

    def test_close_objects(self):
        close_objects(None, 5)
        self.assertFalse(self.uut._closed)
        close_objects(self.uut)
        self.assertTrue(self.uut._closed)
