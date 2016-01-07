import unittest

from pyprint.ColorPrinter import ColorPrinter


class TestColorPrinter(ColorPrinter):

    def _print_colored(self, output, color=None, **kwargs):
        pass

    def _print_uncolored(self, output, **kwargs):
        raise NotImplementedError


class ColorPrinterTest(unittest.TestCase):

    def test_printer_interface(self):
        uut = ColorPrinter()

        with self.assertRaises(NotImplementedError):
            uut.print('test')

        with self.assertRaises(NotImplementedError):
            uut.print('test', color='green')

    def test_force_uncolored(self):
        uut = TestColorPrinter(False)
        with self.assertRaises(NotImplementedError):
            uut.print('test', color='green')

        uut = TestColorPrinter()
        # Doesn't raise
        uut.print('test', color='green')
