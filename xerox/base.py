# -*- coding: utf-8 -*-
import sys

if sys.version_info[0] < 3:
    unicode_type = unicode
else:
    unicode_type = str


class ToolNotFound(Exception):
    """A needed tool was not found."""


class Pywin32NotFound(ToolNotFound):
    """PyWin32 must be installed."""


class ClrNotFound(ToolNotFound):
    """clr must be installed."""


class XcodeNotFound(ToolNotFound):
    """xcode must be installed."""


class XclipNotFound(ToolNotFound):
    """xclip must be installed.
       On Ubuntu,
       $ apt-get install xclip
    """
