""" Copy + Paste in Windows
"""

# found @ http://code.activestate.com/recipes/150115/

import sys

from .base import *

try:
    import win32clipboard as clip
    import win32con
except ImportError as why:
    raise Pywin32NotFound


def copy(string):
    """Copy given string into system clipboard."""

    if not isinstance(string, unicode_type):
        raise ValueError('Expected unicode string, got bytes.')

    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardData(win32con.CF_UNICODETEXT, string)
    clip.CloseClipboard()

    return


def paste():
    """Returns system clipboard contents."""

    clip.OpenClipboard()
    d = clip.GetClipboardData(win32con.CF_UNICODETEXT)
    clip.CloseClipboard()
    return d
