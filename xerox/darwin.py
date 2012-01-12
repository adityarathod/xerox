# -*- coding: utf-8 -*-

""" Copy + Paste in OS X
"""


import subprocess

from .base import *


def copy(string):
    """Copy given string into system clipboard."""
    try:
        subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE).communicate(
                string.encode("utf-8"))
    except OSError as why:
        raise XcodeNotFound
    
    return
   
    
def paste():
    """Returns system clipboard contents."""
    try:
        return subprocess.check_output('pbpaste').decode("utf-8")
    except OSError as why:
        raise XcodeNotFound
    
