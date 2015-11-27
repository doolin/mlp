require_relative 'spec_helper'

RSpec.describe NBClassifier do
  before :all do
    @classifier = NBClassifier.new
    @documents = [
      ["one", "two", 'three'],
      ['three', 'four', 'five']
    ]
  end

  it "creates a vocabulary from documents" do
    vocabulary = @classifier.create_vocabulary(@documents)
    expected = ['one', 'two', 'three', 'four', 'five']
    expect(vocabulary).to eq expected
  end
end
