from .core import *

import sys


def main():
    """ Entry point for cli. """
    if sys.argv[1:]:  # called with input arguments
        copy(' '.join(sys.argv[1:]))
    elif not sys.stdin.isatty():  # piped in input
        copy(''.join(sys.stdin.readlines()).rstrip('\n'))
    else:  # paste output
        print(paste())
