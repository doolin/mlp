#!/usr/bin/env python

# pylint: disable=missing-docstring

import sys
import random

sys.path.append('./lib')
import is_neural as is_neural

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
# 10,000 iterations seems enough to converge [from the book]
# for __ in range(10000):
for __ in range(1000):
    for input_vector, target_vector in zip(inputs, targets):
        # print input_vector
        # print target_vector
        # is_neural.foobar(network, input_vector, target_vector)
        is_neural.backpropagate(network, input_vector, target_vector)

def predict(input):
    return is_neural.feed_forward(network, input)[-1]

# [0.026, 0.0, 0.0, 0.018, 0.001, 0.0, 0.0, 0.967, 0.0, 0.0]
print predict(inputs[7])

predict([
    0,1,1,1,0, # .@@@
    0,0,0,1,1, # ...@@
    0,0,1,1,0, # ..@@
    0,0,0,1,1, # ...@@
    0,1,1,1,0]) # .@@@.
# [0.0, 0.0, 0.0, 0.92, 0.0, 0.0, 0.0, 0.01, 0.0, 0.12]

predict([
    0,1,1,1,0, # .@@@
    1,0,0,1,1, # @..@@
    0,1,1,1,0, # .@@@
    1,0,0,1,1, # @..@@
    0,1,1,1,0]) # .@@@.
# [0.0, 0.0, 0.0, 0.0, 0.0, 0.55, 0.0, 0.0, 0.93, 1.0]

import matplotlib.pyplot as plt
import matplotlib as mpl

weights = network[0][0]
abs_weights = map(abs, weights)

grid = [abs_weights[row:(row+5)]
        for row in range(0,25,5)]

ax = plt.gca()

ax.imshow(grid,
          cmap=mpl.cm.binary,
          interpolation='none')

def patch(x, y, hatch, color):
    """return a matplotlib 'patch' object with the specified
    location, crosshatch pattern and color"""
    return mpl.patches.Rectangle((x-0.5, y-0.5), 1, 1,
        hatch=hatch, fill=False, color=color)

for i in range(5):
    for j in range(5):
        if weights[5*i + j] <  0:
            # add black and white hatches, so visible whether dark or light
            ax.add_patch(patch(j, i, '/', "white"))
            ax.add_patch(patch(j, i, '\\', "black"))

# plt.show()

left_column_only = [1, 0, 0, 0, 0] * 5
print is_neural.feed_forward(network, left_column_only)[0][0] # 10

center_middle_row = [0, 0, 0, 0, 0] * 2 + [0, 1, 1, 1, 0] + [0, 0, 0, 0, 0] * 2
print feed_forward(network, center_middle_row)[0][0] # 0.95

right_column_only = [0, 0, 0, 0, 0] * 5
print feed_forward(network, right_column_only)[0][0] # 0.0

my_three = [
    0,1,1,1,0, # .@@@
    0,0,0,1,1, # ...@@
    0,0,1,1,0, # ..@@
    0,0,0,1,1, # ...@@
    0,1,1,1,0] # .@@@.

sigmoid(.121 * -11.61 + 1 * -2.17 + 1 * 9.31 - 1.38 * 1 - 0 * 11.47 - 1.92)

