# -*- coding: utf-8 -*-

""" Copy + Paste in Linux
"""

import subprocess
from .base import *


def copy(string):
    """Copy given string into system clipboard."""
    try:
        _cmd = ["xclip", "-selection", "clipboard"]
        subprocess.Popen(_cmd, stdin=subprocess.PIPE).communicate(unicode(string))
        return
    except OSError as why:
        raise XclipNotFound
    
def paste():
    """Returns system clipboard contents."""
    try:
        return unicode(subprocess.Popen(["xclip", "-selection", "clipboard", "-o"], stdout=subprocess.PIPE).communicate()[0])
    except OSError as why:
        raise XclipNotFound

