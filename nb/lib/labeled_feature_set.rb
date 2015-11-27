class LabeledFeatureSet
  attr_accessor :label, :features

  def initialize(label:, features:)
    @label = label
    @features = features
  end
end
