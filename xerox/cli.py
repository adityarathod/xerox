""" Copy + Paste in Windows
"""

# found @ http://code.activestate.com/recipes/150115/

from .base import * 

try:
    import clr 
    clr.AddReference('PresentationCore')
    import System.Windows.Clipboard as clip
except ImportError as why:
    raise ClrNotFound


def copy(string): 
    """Copy given string into system clipboard."""

    clip.SetText(string)
    return
    

def paste():
    """Returns system clipboard contents."""

    if clip.ContainsText():
        return clip.GetText()
    
    return None 

 
