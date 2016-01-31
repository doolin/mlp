# pylint: disable=missing-docstring

import numpy

def step_function(x): #  pylint: disable=invalid-name
    return 1 if x >= 0 else 0

def perceptron_output(weights, bias, x):
    """returns 1 if the perceptron 'fires', 0 if not"""
    calculation = numpy.dot(weights, x) + bias
    return step_function(calculation)
