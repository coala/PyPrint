# -*- coding: utf-8 -*-
import colorama
from termcolor import colored

from pyprint.ColorPrinter import ColorPrinter


class ConsolePrinter(ColorPrinter):
    """
    A simple printer for the console that supports colors.

    Note that pickling will not pickle the output member.
    """
    colorama_initialized = False

    def __init__(self, print_colored=None):
        """
        Instantiates a new ConsolePrinter.

        :param print_colored: Whether to print with colors or not. If None use
                              colors if supported.
        """
        ColorPrinter.__init__(self, print_colored)
        if not ConsolePrinter.colorama_initialized:
            colorama.init()
            ConsolePrinter.colorama_initialized = True

    def _print_uncolored(self, output, **kwargs):
        print(output, end="")

    def _print_colored(self, output, color, **kwargs):
        print(colored(output, color), end="")
