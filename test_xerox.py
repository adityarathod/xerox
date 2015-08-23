#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xerox
import unittest
import sys
import time

if sys.version_info[0] < 3:
    str = unicode


class BasicAPITestCase(unittest.TestCase):
    def setUp(self):
        """
        Note the apostrophe below is actually Unicode U+2019 'RIGHT SINGLE QUOTATION MARK', to
        test for unicode decode errors
        """
        # unicode test string
        self.text = b'And now it\xe2\x80\x99s time for something completely different.'.decode(
            'utf-8')

        # add current time (to avoid problems where the clipboard content was correct for the wrong reason)
        self.text += str(time.time())

    def test_copy_and_paste(self):
        # copy
        self.assertIsInstance(self.text, str)
        xerox.copy(self.text)

        # paste
        got = xerox.paste()
        self.assertIsInstance(got, str)
        self.assertEqual(got, self.text)

    def test_no_unicode(self):
        with self.assertRaises(ValueError):
            xerox.copy(b'This is a byte string.')


if __name__ == '__main__':
    unittest.main()
