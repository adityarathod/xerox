import sys

if sys.platform == 'darwin':
    from .darwin import *

elif sys.platform == 'win32':
    try:
        from .win import *
    except ImportError:
        from .tkinter import *

elif sys.platform == 'cli':
    from .cli import *

else:
    from .x11 import *
