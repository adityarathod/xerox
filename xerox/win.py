""" Copy + Paste in Windows
"""

# found @ http://code.activestate.com/recipes/150115/

from .base import * 

try:
    import win32clipboard as clip
    import win32con
except ImportError, why:
    raise Pywin32NotFound


def copy(string): 
    """Copy given string into system clipboard."""

    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardData(1, string) 
    clip.CloseClipboard()

    return
    

def paste():
    """Returns system clipboard contents."""

    clip.OpenClipboard() 
    d = clip.GetClipboardData(win32con.CF_TEXT) 
    clip.CloseClipboard() 
    return d 

 
