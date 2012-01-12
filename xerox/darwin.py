# -*- coding: utf-8 -*-

""" Copy + Paste in OS X
"""


import subprocess

from .base import *


def copy(string):
    """Copy given string into system clipboard."""
    try:
        subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE).communicate(str(unicode(string)))
    except OSError as why:
        raise XcodeNotFound
    
    return
   
    
def paste():
    """Returns system clipboard contents."""
    try:
        return unicode(subprocess.check_output('pbpaste'))
    except OSError as why:
        raise XcodeNotFound
    
