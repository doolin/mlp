#!/usr/bin/env python

# pylint: disable=missing-docstring

import unittest
import sys

# from numpy import *

sys.path.append('../lib')

import nb #  pylint: disable=import-error
class TestNB(unittest.TestCase):

    def test_tokenize(self):
        message = "foo bar"
        expected = set(['foo', 'bar'])
        actual = nb.tokenize(message)
        self.assertEqual(actual, expected)

    def test_count_words(self):
        training_set = [("foo bar", 1)]
        actual = nb.count_words(training_set)
        expected = {'foo': [1, 0], 'bar': [1, 0]}
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
