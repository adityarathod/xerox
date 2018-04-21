""" Copy + Paste in Windows
"""

# found @ http://code.activestate.com/recipes/150115/

from .base import * 

try:
    import win32clipboard as clip
    import win32con
except ImportError as why:
    raise Pywin32NotFound


def copy(string, **kwargs):
    """Copy given string into system clipboard."""

    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardData(win32con.CF_UNICODETEXT, string) 
    clip.CloseClipboard()

    return

def paste(**kwargs):
    """Returns system clipboard contents."""

    clip.OpenClipboard() 
    try:
        d = clip.GetClipboardData(win32con.CF_UNICODETEXT)
    except TypeError:
        # Handle, "Specified clipboard format is not available"
        # Either clipboard is empty or does NOT contain text
        d = ''
    clip.CloseClipboard() 
    return d 

 
