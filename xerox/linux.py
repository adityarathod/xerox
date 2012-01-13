# -*- coding: utf-8 -*-

""" Copy + Paste in Linux
"""

import subprocess
from .base import *


def copy(string):
    """Copy given string into system clipboard."""
    try:
        _cmd = ["xclip", "-selection", "clipboard"]
        subprocess.Popen(_cmd, stdin=subprocess.PIPE).communicate(
                string.encode('utf-8'))
        return
    except OSError as why:
        raise XclipNotFound
    
def paste():
    """Returns system clipboard contents."""
    try:
        return subprocess.Popen(["xclip", "-selection", "clipboard", "-o"], stdout=subprocess.PIPE).communicate()[0].decode("utf-8")
    except OSError as why:
        raise XclipNotFound

