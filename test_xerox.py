#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xerox
import unittest

class BasicAPITestCase(unittest.TestCase):
    def setUp(self):
        self.text = 'And now for something completely different.'
        
    def test_copy(self):
        xerox.copy(self.text)
        self.assertEqual(xerox.paste(), self.text)
        
    def test_paste(self):
        xerox.copy(self.text)
        self.assertEqual(xerox.paste(), self.text)
        
        
if __name__ == '__main__':
    unittest.main()