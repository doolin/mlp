require_relative 'spec_helper'

RSpec.describe LabeledFeatureSet do
  before :example  do
    @lfs = LabeledFeatureSet.new label: 'male', features: [6, 180, 12]
  end

  it 'instantiates a LabeledFeatureSet' do
    expect(@lfs).not_to be_nil
    expect(@lfs.label).to eq 'male'
    expect(@lfs.features).to eq [6, 180, 12]
  end
end
