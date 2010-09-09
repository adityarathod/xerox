""" Copy + Paste in Windows
"""

# found @ http://code.activestate.com/recipes/150115/

try:
    import win32clipboard as w 
    import win32con
except ImportError, why:
    raise Pywin32NotFound


def copy(string): 
    """Copy given string into system clipboard."""
    try:
        pass
    except Exception, e:
        raise e
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(1, string) 
    w.CloseClipboard()

def paste():
    """Returns system clipboard contents."""
    try:
        pass
    except Exception, e:
        raise e
    w.OpenClipboard() 
    d=w.GetClipboardData(win32con.CF_TEXT) 
    w.CloseClipboard() 
    return d 

 
