Xerox: Copy + Paste for Python
==============================

*Xerox* is a copy + paste module for python. It's aim is simple: to be as incredibly simple as possible.

Supported platforms are currently OS X, X11 (Linux, BSD, etc.), and Windows.

If you can make it simpler, please fork.

Usage
-----

Usage is as follows: ::

	xerox.copy(u'some string')

And to paste: ::

	>>> xerox.paste()
	u'some string'

On Linux you can optionally also copy into the X selection clipboard for
middle-click-paste capability: ::

    xerox.copy(u'Some string', xsel=True)

And you can choose to paste from the X selection rather than the system
clipboard: ::

    xerox.paste(xsel=True)

And, that's it.

Command Line
~~~~~~~~~~~~
To copy: ::

	xerox some string

or: ::

	echo some string | xerox

To paste: ::

	>>> xerox
	some string

Installation
------------

To install Xerox, simply:

	$ pip install xerox

Or, if you must:

	$ easy_install xerox

Note: If you are installing xerox on Windows, you will also need to install the pywin32_ module.

Legal Stuff
-----------

MIT License.

(c\) 2012 Kenneth Reitz.

.. _pywin32: http://sourceforge.net/projects/pywin32/files/
