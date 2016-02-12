import unittest

from pyprint.ConsolePrinter import ConsolePrinter
from pyprint.ContextManagers import retrieve_stdout


class ConsolePrinterTest(unittest.TestCase):

    def test_printing(self):
        self.assertEqual(ConsolePrinter.colorama_initialized, False)
        self.uut = ConsolePrinter(print_colored=True)
        self.assertEqual(ConsolePrinter.colorama_initialized, True)

        with retrieve_stdout() as stdout:
            self.uut.print("\ntest", "message", color="green")
            self.assertRegex(stdout.getvalue(), "\033.*\ntest message.*")

        with retrieve_stdout() as stdout:
            self.uut.print("\ntest", "message", color="greeeeen")
            self.assertEqual(stdout.getvalue(), "\ntest message\n")

        with retrieve_stdout() as stdout:
            self.uut.print("\ntest", "message")
            self.assertEqual(stdout.getvalue(), "\ntest message\n")

        self.uut = ConsolePrinter()
        self.assertEqual(ConsolePrinter.colorama_initialized, True)
