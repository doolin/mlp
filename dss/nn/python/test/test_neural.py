#!/usr/bin/env python

# pylint: disable=missing-docstring,invalid-name

import unittest
import sys

from numpy import *

sys.path.append('../lib')
import neural as neural

# pylint: disable=bad-whitespace
zero_digit = [
    1,1,1,1,1,
    1,0,0,0,1,
    1,0,0,0,1,
    1,0,0,0,1,
    1,1,1,1,1
]
one_digit = [
    0,0,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0
]
two_digit = [
    1,1,1,1,1,
    0,0,0,0,1,
    1,1,1,1,1,
    1,0,0,0,0,
    1,1,1,1,1
]
three_digit = [
    1,1,1,1,1,
    0,0,0,0,1,
    1,1,1,1,1,
    0,0,0,0,1,
    1,1,1,1,1
]
four_digit = [
    1,0,0,0,1,
    1,0,0,0,1,
    1,1,1,1,1,
    0,0,0,0,1,
    0,0,0,0,1
]


class TestNB(unittest.TestCase):

    def test_step_function(self):
        expected = 1
        actual = neural.step_function(1)
        self.assertEqual(actual, expected)

    def test_perceptron_output(self):
        # and gate
        weights = [2, 2]
        bias = -3.0
        x = [1, 1]
        expected = 1.0
        actual = neural.perceptron_output(weights, bias, x)
        self.assertEqual(actual, expected)

        # or gate
        weights = [2, 2]
        bias = -3.0
        x = [1, 0]
        expected = 0.0
        actual = neural.perceptron_output(weights, bias, x)
        self.assertEqual(actual, expected)

    def test_feed_forward(self):
        xor_network = [ # hidden layer
            [[20, 20, -30],
             [20, 20, -10]],
            # output layer
            [[-60, 60, -30]]
        ]

        output = []
        for x in [0, 1]:
            for y in [0, 1]:
                print x, y, neural.feed_forward(xor_network, [x, y])[-1]
                output.append(neural.feed_forward(xor_network, [x, y])[-1])

        print output

if __name__ == '__main__':
    unittest.main()
