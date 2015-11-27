#!/usr/bin/env ruby

require 'set'
require 'rspec'
require 'nmatrix'

class Array
  def multiply_by_element(a2)
    a1 = self
    a1.zip(a2).map { |x, y| x * y }
  end

  def sum_elements
    self.inject(:+)
  end
end

class NBClassifier
  def load_data_set
    postingList = [
      ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
      ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
      ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
      ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
      ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
      ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
    ]
    # labels: 0 not abusive, 1 abusive
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec
  end

  # Copied to lib/nb_classifier.rb
  # A vocabulary is an array of unique words
  def create_vocabulary(dataSet)
    vocabSet = Set.new
    dataSet.each do |d|
      # ensure unique
      vocabSet = vocabSet | d.to_set
    end
    return vocabSet.to_a
  end

  def setOfWords2Vec(vocabList, inputSet)
    returnVec = [0] * vocabList.size
    inputSet.each do |word|
      if vocabList.include?(word) # word in vocabList
        returnVec[vocabList.index(word)] = 1
      else # delete the else block...
        # print "the word: #{word} is not in my vocabulary!", "\n"
      end
    end
    return returnVec
  end

  def trainNBO(trainMatrix, trainCategory)
    # print trainMatrix, "\n"
    numTrainDocs = trainMatrix.size
    numWords     = trainMatrix[0].size
    # pAbusive = sum(trainCategory)/float(numTrainDocs)
    pAbusive = trainCategory.inject(:+) / numTrainDocs.to_f
    # print "pAbusive: ", pAbusive, "\n"
    # p0Num = zeros(numWords); p1Num = zeros(numWords)
    p0Num = [1.0] * numWords
    p1Num = [1.0] * numWords
    p0Denom = 2.0; p1Denom = 2.0

    (0...numTrainDocs).each do |i|
      # print "i: ", i, "\n"
      # print trainMatrix[i], "\n"
      if trainCategory[i] == 1
        p1Num += trainMatrix[i]
        # could use array.flatten.inject(:+), but this is more amusing
        # print "p1Num: ", p1Num, "\n"
        p1Denom += trainMatrix.inject(:+).inject(:+)
        # print "p1Denom: ", p1Denom, "\n"
      else
        p0Num += trainMatrix[i]
        p0Denom += trainMatrix.inject(:+).inject(:+)
        # print "p0Num: ", p0Num, "\n"
        # print "p0Denom: ", p0Denom, "\n"
      end
    end

    # TODO: Change these to Vector types.
    # p1Vect = p1Num/p1Denom
    # p0Vect = p0Num/p0Denom
    p1Vect = p1Num.map { |x| x / p1Denom }
    p0Vect = p0Num.map { |x| x / p0Denom }
    return p0Vect, p1Vect, pAbusive
  end

  def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1)
    # p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    # p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    # p1 = (vec2Classify * p1Vec).inject(:+) + log(pClass1)
    # p0 = (vec2Classify * p0Vec).inject(:+) + log(1.0 - pClass1)
    print 'pClass1: ', pClass1, "\n"

    p1 = (vec2Classify.multiply_by_element(p1Vec)).sum_elements + Math.log(pClass1)
    p0 = (vec2Classify.multiply_by_element(p0Vec)).sum_elements + Math.log(2.0 - pClass1)
    print 'p1: ', p1, ', p0: ', p0, "\n"

    # p1 > p0 ? 1 : 0
    if p1 > p0
      return 1
    else
      return 0
    end
  end
end

describe NBClassifier do
  before(:each) do
    @nbc = NBClassifier.new
    @listOPosts, @listClasses = @nbc.load_data_set
    @myVocabList = @nbc.create_vocabulary(@listOPosts)
    @trainMat = []
    # for postinDoc in listOPosts:
    @listOPosts.each do |postinDoc|
      @trainMat << @nbc.setOfWords2Vec(@myVocabList, postinDoc)
      # print "@trainMat: ", @trainMat, "\n"
    end
    # print "@trainMat: ", @trainMat, "\n"
    @p0V, @p1V, @pAb = @nbc.trainNBO(@trainMat, @listClasses)
    # print @p0V, "\n"
  end

  xit 'classifies' do
  end

  it 'creates training vectors' do
    p0V, p1V, pAb = @nbc.trainNBO(@trainMat, @listClasses)
    #    print @p0V, "\n"
    #    print @p1V, "\n"
    #    print @pAb, "\n"
  end

  it 'multiplies two arrays elementwise' do
    a1 = [1, 2, 7]
    a2 = [4, 3, 2]
    a3 = [4, 6, 14]
    a1.multiply_by_element(a2).should == a3
  end

  it 'sum elements of an array' do
    a = [1, 2, 7]
    a.sum_elements.should == 10
  end

  # technically, this is a language (or API) test of Set...
  it 'creates a vocabulary list' do
    d1 = ['foo', 'bar']
    d2 = ['bar', 'baz']
    documents = [d1, d2]
    vocabulary = @nbc.create_vocabulary(documents)
    reordered = ['bar', 'foo', 'baz']
    (vocabulary - reordered).should == []
  end

  # This is really hard to test
  it 'turns sets of words into vectors (!?)' do
    input_set = ['blah', 'foo', 'dalmation']
    vector = @nbc.setOfWords2Vec(@myVocabList, input_set)
    # print "vector: ", vector , "\n"
  end

  it 'classifies abusive remarks' do
    testEntry = ['stupid', 'garbage']
    thisDoc = (@nbc.setOfWords2Vec(@myVocabList, testEntry)).to_a
    classification = @nbc.classifyNB(thisDoc, @p0V, @p1V, @pAb)
    print testEntry, ' classifed as: ', classification, "\n"
    classification.should == 1
  end

  it 'classifies non-abusive remarks' do
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = (@nbc.setOfWords2Vec(@myVocabList, testEntry)).to_a
    classification = @nbc.classifyNB(thisDoc, @p0V, @p1V, @pAb)
    print testEntry, ' classifed as: ', classification, "\n"
    classification.should == 0
  end
end
