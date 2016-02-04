# -*- coding: utf-8 -*-

""" Copy + Paste in X11
"""

import subprocess
from .base import *


def copy(string, xsel=False):
    """Copy given string into system clipboard. If 'xsel' is True, this
    will also copy into the primary x selection for middle click."""
    try:
        _cmd = ["xclip", "-selection", "clipboard"]
        subprocess.Popen(_cmd, stdin=subprocess.PIPE).communicate(
                string.encode('utf-8'))
        if xsel:
            _cmd = ["xclip", "-selection", "primary"]
            subprocess.Popen(_cmd, stdin=subprocess.PIPE).communicate(
                    string.encode('utf-8'))
    except OSError as why:
        raise XclipNotFound

def paste(xsel=False):
    """Returns system clipboard contents."""
    selection = "primary" if xsel else "clipboard"
    try:
        return subprocess.Popen(["xclip", "-selection", selection, "-o"], stdout=subprocess.PIPE).communicate()[0].decode("utf-8")
    except OSError as why:
        raise XclipNotFound

