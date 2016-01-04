#!/usr/bin/env python

# pylint: disable=missing-docstring

import unittest
import sys

# from numpy import *

sys.path.append('../lib')
import nb

class TestNB(unittest.TestCase):

    def test_tokenize(self):
        message = "foo bar"
        expected = set(['foo', 'bar'])
        actual = nb.tokenize(message)
        print actual
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
