import colorama
from termcolor import colored

from pyprint.ColorPrinter import ColorPrinter


class ConsolePrinter(ColorPrinter):
    """
    A simple printer for the console that supports colors.

    Note that pickling will not pickle the output member.
    """

    def __init__(self, print_colored=None):
        """
        Instantiates a new ConsolePrinter.

        :param print_colored: Whether to print with colors or not. If None use
                              colors if supported.
        """
        ColorPrinter.__init__(self, print_colored)
        colorama.init()

    def _print_uncolored(self, output, **kwargs):
        print(output, end="")

    def _print_colored(self, output, color, **kwargs):
        print(colored(output, color), end="")
