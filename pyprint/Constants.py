# -*- coding: utf-8 -*-
import os


PYPRINT_ROOT = os.path.dirname(__file__)
VERSION_FILE = os.path.join(PYPRINT_ROOT, "VERSION")
with open(VERSION_FILE, 'r') as ver:
    VERSION = ver.readline().strip()
