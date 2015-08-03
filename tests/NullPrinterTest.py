import unittest

from pyprint.NullPrinter import NullPrinter


class NullPrinterTest(unittest.TestCase):
    def test_non_printing(self):
        self.uut = NullPrinter()
        self.assertEqual(self.uut.print("anything"), None)
        self.assertEqual(self.uut.print("anything", color="red"), None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
