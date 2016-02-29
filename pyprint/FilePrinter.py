# -*- coding: utf-8 -*-
from pyprint.Printer import Printer


class FilePrinter(Printer):
    """
    This is a simple printer that prints everything to a file. Note
    that everything will be appended.
    """

    def __init__(self, filehandle):
        """
        Creates a new FilePrinter. If the directory of the given file doesn't
        exist or if there's any access problems, an exception will be thrown.

        :param filehandle: A file-like object to put the data into. It's write
                           method will be invoked.
        """
        Printer.__init__(self)

        if not hasattr(filehandle, "write"):
            raise TypeError("filehandle must be a file like object "
                            "i.e. provide a write method.")

        self.file = filehandle

    def _print(self, output, **kwargs):
        self.file.write(output)
