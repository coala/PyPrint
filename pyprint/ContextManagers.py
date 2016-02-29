# -*- coding: utf-8 -*-
from contextlib import contextmanager, closing
from io import StringIO
import sys


@contextmanager
def replace_stdout(replacement):
    """
    Replaces stdout with the replacement, yields back to the caller and then
    reverts everything back.

    :param replacement: A file IO object to replace the stdout.
    """
    _stdout = sys.stdout
    sys.stdout = replacement
    try:
        yield
    finally:
        sys.stdout = _stdout


@contextmanager
def retrieve_stdout():
    """
    Yields a StringIO object from which you can read everything that was
    printed to stdout. (It won't be printed to the real stdout!)

    Example usage:

    with retrieve_stdout() as stdout:
        print("something")  # Won't print to the console
        what_was_printed = stdout.getvalue()  # Save the value
    """
    with closing(StringIO()) as sio, replace_stdout(sio):
        yield sio
