from .core import *

import sys
import os
import stat

def main():
    """ Entry point for cli. """
    mode = os.fstat(0).st_mode
    if sys.argv[1:]:  # called with input arguments
        copy(' '.join(sys.argv[1:]))
    elif stat.S_ISFIFO(mode) or stat.S_ISREG(mode):  # piped in input
        copy('\n'.join(sys.stdin.readlines()))
    else:  # paste output
        print(paste())
