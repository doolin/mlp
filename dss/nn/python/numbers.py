#!/usr/bin/env python

# pylint: disable=missing-docstring

import sys

sys.path.append('./lib')
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
five_digit = [
    1,1,1,1,1,
    1,0,0,0,0,
    1,1,1,1,1,
    0,0,0,0,1,
    1,1,1,1,1
]
six_digit = [
    1,1,1,1,1,
    1,0,0,0,0,
    1,1,1,1,1,
    1,0,0,0,1,
    1,1,1,1,1
]
seven_digit = [
    1,1,1,1,1,
    0,0,0,0,1,
    0,0,0,0,1,
    0,0,0,0,1,
    0,0,0,0,1
]
eight_digit = [
    1,1,1,1,1,
    1,0,0,0,1,
    1,1,1,1,1,
    1,0,0,0,1,
    1,1,1,1,1
]
nine_digit = [
    1,1,1,1,1,
    1,0,0,0,1,
    1,1,1,1,1,
    0,0,0,0,1,
    1,1,1,1,1
]

targets = [[1 if i == j else 0 for i in range(10)]
           for j in range(10)]

random.seed(0)   # to get repeatable results
input_size = 25  # each input is a vector of length 25
num_hidden = 5   # we'll have 5 neurons in the hidden layer
output_size = 10 # we need 10 outputs for each input


