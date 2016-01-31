#!/usr/bin/env python

# pylint: disable=missing-docstring

import unittest
import sys

from numpy import *

sys.path.append('../lib')
import neural as neural


class TestNB(unittest.TestCase):

    def test_step_function(self):
        expected = 1
        actual = neural.step_function(1)
        self.assertEqual(actual, expected)

    def test_perceptron_output(self):
        weights = [1, 1]
        bias = 1.0
        x = [1, 2]
        expected = 1.0
        actual = neural.perceptron_output(weights, bias, x)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
