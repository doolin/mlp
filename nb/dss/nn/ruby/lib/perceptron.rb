require 'nmatrix'

class Perceptron
  def initialize(weights:, bias:)
    @weights = weights
    @bias = bias
  end

  def step_function(x)
    x >= 0 ? 1 : 0
  end

  def think(u)
    step_function(@weights.dot(u).to_f + @bias)
  end

  def self.sigmoid(t)
    1.0 / (1.0 + Math.exp(-t))
  end

  def self.neuron_output(weights, inputs)
    sigmoid(weights.dot(inputs).to_f)
  end
end
