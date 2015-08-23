# -*- coding: utf-8 -*-
""" Copy + Paste in OS X
"""

import subprocess
import os

from .base import *


def copy(string):
    """Copy given string into system clipboard."""
    if not isinstance(string, unicode_type):
        raise ValueError('Expected unicode string, got bytes.')

    try:
        subprocess.Popen(['pbcopy'],
                         stdin=subprocess.PIPE).communicate(
                             string.encode("utf-8"))
    except OSError as why:
        raise XcodeNotFound

    return


def paste():
    """Returns system clipboard contents."""
    try:
        #Tell the IO system to decode IPC IO with utf-8,
        #to prevent UnicodeDecodeErrors on python3
        os.environ['LANG'] = 'en_US.utf-8'
        return subprocess.Popen(
            ['pbpaste'],
            stdout=subprocess.PIPE).communicate()[0].decode('utf-8')

    except OSError as why:
        raise XcodeNotFound
