require_relative '../lib/perceptron'

describe Perceptron do
  it "instantiates" do
    expect(Perceptron.new).not_to be_nil
  end
end

