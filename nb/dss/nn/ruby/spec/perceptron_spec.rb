require_relative '../lib/perceptron'

describe Perceptron do
  subject { Perceptron.new }

  it "instantiates" do
    expect(Perceptron.new).not_to be_nil
  end

  it "fires the step function for x > 1" do
    expect(subject.step_function(3)).to be 1
  end

  it "fires the step function for x < 1" do
    expect(subject.step_function(0.2)).to be 0
  end
end

