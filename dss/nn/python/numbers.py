#!/usr/bin/env python

# pylint: disable=missing-docstring

import sys
import random

sys.path.append('./lib')
import is_neural as neural
# from is_neural import foobar

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

inputs = [
    zero_digit,
    one_digit,
    two_digit,
    three_digit,
    four_digit,
    five_digit,
    six_digit,
    seven_digit,
    eight_digit,
    nine_digit
]

targets = [[1 if i == j else 0 for i in range(10)]
           for j in range(10)]

random.seed(0)   # to get repeatable results
input_size = 25  # each input is a vector of length 25
num_hidden = 5   # we'll have 5 neurons in the hidden layer
output_size = 10 # we need 10 outputs for each input

# each hidden neuron has one weight per input, plus a bias weight
hidden_layer = [[random.random() for __ in range(input_size + 1)]
                for __ in range(num_hidden)]

# each output neuron has one weight per hidden neuron, plus a bias weight
output_layer = [[random.random() for __ in range(num_hidden + 1)]
                for __ in range(output_size)]

# the network starts out with random weights
network = [hidden_layer, output_layer]

# train it using the back propagation algorithm
# 10,000 iterations seems enough to converge
for __ in range(10000):
    for input_vector, target_vector in zip(inputs, targets):
        neural.foobar(network, input_vector, target_vector)

def predict(input):
    return neural.feed_forward(network, input)[-1]
