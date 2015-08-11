import importlib
import platform
import unittest

import pyprint.ConsolePrinter
from pyprint.ConsolePrinter import ConsolePrinter
from pyprint.ContextManagers import retrieve_stdout


class ConsolePrinterTest(unittest.TestCase):
    def setUp(self):
        self._platform_system = platform.system

    def tearDown(self):
        platform.system = self._platform_system

    @staticmethod
    def change_platform_system(platf):
        platform.system = lambda: platf
        importlib.reload(pyprint.ConsolePrinter)
        ConsolePrinter = pyprint.ConsolePrinter.ConsolePrinter

    def test_printing(self):
        self.uut = ConsolePrinter(print_colored=True)

        with retrieve_stdout() as stdout:
            self.uut.print("\ntest", "message", color="green")
            self.assertRegex(stdout.getvalue(), "\033.*\ntest message.*")

        with retrieve_stdout() as stdout:
            self.uut.print("\ntest", "message", color="greeeeen")
            self.assertEqual(stdout.getvalue(), "\ntest message\n")

        with retrieve_stdout() as stdout:
            self.uut.print("\ntest", "message")
            self.assertEqual(stdout.getvalue(), "\ntest message\n")

    def test_color_support(self):
        self.change_platform_system("Linux")
        self.assertTrue(ConsolePrinter().supports_colors)

        self.change_platform_system("Windows")
        self.assertFalse(ConsolePrinter().supports_colors)

        self.change_platform_system("Darwin")
        self.assertFalse(ConsolePrinter().supports_colors)

        self.change_platform_system("UNKNOWN")
        self.assertFalse(ConsolePrinter().supports_colors)
