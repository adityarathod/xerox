import sys

__title__ = 'xerox'
__version__ = '0.2.1'
__author__ = 'Kenneth Reitz'
__license__ = 'MIT'

if sys.platform == 'darwin':
    from .darwin import *
    
elif sys.platform == 'linux2':
    from .linux import *
    
elif sys.platform == 'win32':
    from .win import *
