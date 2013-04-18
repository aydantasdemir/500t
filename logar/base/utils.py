# -*- coding: utf8 -*-
import os


def here(arg):
    return os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', arg))
