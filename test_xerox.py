#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xerox
import unittest
import sys


class BasicAPITestCase(unittest.TestCase):
    def setUp(self):
        """
        Note the apostrophe below is actually Unicode U+2019 'RIGHT SINGLE QUOTATION MARK', to
        test for unicode decode errors
        """
        if sys.version_info >= (3, 0):
            self.text = 'And now it’s time for something completely different.'
        else:
            #Python <= 3.3 doesn't support u'' literals, so use the unicode constructor instead
            #self.text = u'And now it’s time for something completely different.'
            self.text = unicode('And now it\xe2\x80\x99s time for something completely different.', encoding='utf-8')
        
    def test_copy(self):
        xerox.copy(self.text)
        self.assertEqual(xerox.paste(), self.text)
        
    def test_paste(self):
        xerox.copy(self.text)
        self.assertEqual(xerox.paste(), self.text)
        
        
if __name__ == '__main__':
    unittest.main()