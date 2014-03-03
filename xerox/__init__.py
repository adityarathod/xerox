from .core import *

import sys

def main():
    """ Entry point for cli. """
    if sys.argv[1:]:  # called with input arguments
        copy(' '.join(sys.argv[1:]))
    elif not sys.stdin.isatty():  # piped in input
        copy('\n'.join(sys.stdin.readlines()))
    else:  # paste output
        print(paste())
