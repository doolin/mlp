require_relative '../lib/perceptron'

describe Perceptron do
  let(:weights) { NMatrix.new([4], [1, 2, 3, 4]) }
  let(:bias) { 0 }
  subject { Perceptron.new(weights: weights, bias: bias) }

  it 'instantiates' do
    expect(subject).not_to be_nil
  end

  it 'fires the step function for x > 1' do
    expect(subject.step_function(3)).to be 1
  end

  it 'fires the step function for x < 1' do
    expect(subject.step_function(0.2)).to be 0
  end

  it "'thinks' when given a new vector" do
    u = NMatrix.new([4], [1, 2, 3, 4])
    expect(subject.think(u)).to be 1
  end

  it "'thinks' when given a new vector" do
    u = NMatrix.new([4], [0, 0, 0, 0])
    expect(subject.think(u)).to be 0
  end
end
