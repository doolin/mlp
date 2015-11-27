class NBClassifier
  # A vocabulary is an array of unique words
  def create_vocabulary(dataSet)
    vocabSet = Set.new
    dataSet.each do |d|
      # ensure unique
      vocabSet = vocabSet | d.to_set
    end
    return vocabSet.to_a
  end
end
