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

  def self.feed_forward(neural_network, input_vector)
    outputs = []

    neural_network.each do |layer|
      input_with_bias = input_vector + [1]
      # this is borked, do the python first
      layer.each do |neuron|
        output = neuron_output(neuron, input_with_bias)
      end
      outputs.append(output)
    end
    input_vector = output
  end
end
