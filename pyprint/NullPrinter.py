# -*- coding: utf-8 -*-
from pyprint.Printer import Printer


class NullPrinter(Printer):
    """
    A printer that dismisses all printed messages.
    """

    def __init__(self):
        """
        Instantiates a new NullPrinter.
        """
        Printer.__init__(self)

    def _print(self, output, **kwargs):
        return
