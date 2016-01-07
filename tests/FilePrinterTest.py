from tempfile import TemporaryFile
import unittest

from pyprint.FilePrinter import FilePrinter


class FilePrinterTest(unittest.TestCase):

    def test_invalid_construction(self):
        self.assertRaises(TypeError, FilePrinter, 5)

    def test_printing(self):
        self.file = TemporaryFile("w+")
        self.uut = FilePrinter(self.file)

        self.uut.print("Test value")

        self.uut = FilePrinter(self.file)
        self.uut.print("Test", "value2")

        self.file.seek(0)
        lines = self.file.readlines()

        self.assertEqual(lines, ["Test value\n", "Test value2\n"])
