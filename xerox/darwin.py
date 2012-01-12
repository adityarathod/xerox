# -*- coding: utf-8 -*-

""" Copy + Paste in OS X
"""


import subprocess
import commands

from .base import *


def copy(string):
    """Copy given string into system clipboard."""
    try:
        subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE).communicate(str(unicode(string)))
    except Exception, why:
        raise XcodeNotFound
    
    return
   
    
def paste():
    """Returns system clipboard contents."""
    try:
        return unicode(commands.getoutput('pbpaste'))
    except Exception, why:
        raise XcodeNotFound
    
