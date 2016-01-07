import unittest

from pyprint.StringPrinter import StringPrinter


class StringPrinterTest(unittest.TestCase):

    def test_construction(self):
        uut = StringPrinter()
        self.assertEqual(uut.string, "")

    def test_printing(self):
        uut = StringPrinter()
        self.assertEqual(uut.string, "")

        uut.print("ABC")
        self.assertEqual(uut.string, "ABC\n")

        uut.print("XYZ")
        self.assertEqual(uut.string, "ABC\nXYZ\n")

        uut.print("\nHello World.")
        self.assertEqual(uut.string, "ABC\nXYZ\n\nHello World.\n")

    def test_clear(self):
        uut = StringPrinter()
        self.assertEqual(uut.string, "")

        uut.clear()
        self.assertEqual(uut.string, "")

        uut.print("1")
        self.assertEqual(uut.string, "1\n")
        uut.clear()
        self.assertEqual(uut.string, "")

        uut.print(1000 * "#")
        self.assertEqual(uut.string, 1000 * "#" + "\n")
        uut.clear()
        self.assertEqual(uut.string, "")
