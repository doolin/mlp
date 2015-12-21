class NBClassifier

  # A vocabulary is an array of unique words
  def create_vocabulary(documents)
    vocabulary = Set.new
    documents.each do |d|
      vocabulary = vocabulary | d.to_set # ensure unique
    end
    vocabulary.to_a
  end
end
