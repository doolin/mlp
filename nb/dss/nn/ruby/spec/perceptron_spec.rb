require_relative '../lib/perceptron'

describe Perceptron do
  let(:weights) { NMatrix.new([2], [2, 2]) }
  let(:bias) { 0 }
  subject { Perceptron.new(weights: weights, bias: bias) }

  it 'instantiates' do
    expect(subject).not_to be_nil
  end

  describe "#step_function" do
    it 'fires the step function for x >= 0' do
      expect(subject.step_function(3)).to be 1
    end

    it 'fires the step function for x < 0' do
      expect(subject.step_function(-0.2)).to be 0
    end
  end

  describe "AND gate" do
    let(:bias) { -3 }
    subject { Perceptron.new(weights: weights, bias: bias) }

    it "return 1 for both inputs 1" do
      u = NMatrix.new([2], [1, 1])
      expect(subject.think(u)).to be 1
    end

    it "return 0 for [1, 0]" do
      u = NMatrix.new([2], [1, 0])
      expect(subject.think(u)).to be 0
    end

    it "return 0 for [0, 1]" do
      u = NMatrix.new([2], [0, 1])
      expect(subject.think(u)).to be 0
    end
  end

  describe "OR gate" do
  end
end
