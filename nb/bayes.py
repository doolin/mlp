#!/usr/bin/env python

from numpy import *
import unittest


# page 67
def loadDataSet():
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


# page 67, 68
# create a list of unique words from the dataSet argument.
# The `|` is a union operator for sets. For example,
# >>> set([1, 2, 5]) | set([1, 3]) => set([1, 2, 3, 5])
# https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
# a better name for this function would be create_unique_words.
# In a Ruby class, this would def unique_words; @unique_words ||= create_unique_words; end
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


# pages 67, 68, 69
# From the top of page 69, the author states this is the function which creates
# a feature for every word in a list.
# A better name for this function might be `create_features`, again, the code
# is written from an implementation perspective rather than an algorithm
# perspective.
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my vocabulary!" % word
    return returnVec


# page 69
def trainNBO(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0]) # numWords is number of features?
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = zeros(numWords) # => array([0., ..., 1.])
    p1Num = zeros(numWords)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocs): # [0, 1, 2, ..., numTrainingDocs]
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    print "p0Denom: ", p0Denom
    print "p1Denom: ", p1Denom
    p1Vect = p1Num / p1Denom
    p0Vect = p0Num / p0Denom
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    # print "testingNB()..."
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = [] # list of lists, e.g., [[...], ..., [...]]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNBO(trainMat, listClasses)
    # print "p0V: ", p0V, "\n"
    # print "p1V: ", p1V, "\n"
    # print "pAb: ", pAb, "\n"
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classifed as: ', classifyNB(thisDoc, p0V, p1V, pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classifed as: ', classifyNB(thisDoc, p0V, p1V, pAb)

testingNB()

class TestNB(unittest.TestCase):
    def test_setOfWords2Vec(self):
        # listOPosts is actually...
        # listClasses is actually a list of labels for the data in listOPosts
        listOPosts, listClasses = loadDataSet()
        myVocabList = createVocabList(listOPosts)
        features = setOfWords2Vec(myVocabList, listOPosts[0])
        expected = [
            0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1
        ]
        self.assertEqual(features, expected)

    def test_createVocabList(self):
        dataSet = [
            ['stupid', 'garbage'],
            ['love', 'puppies']
        ]
        expected = ['stupid', 'garbage', 'love', 'puppies']
        word_list = createVocabList(dataSet)
        self.assertTrue(set(word_list) == set(expected))
        # don't want duplicate elements
        self.assertTrue(len(word_list) == len(expected))

    def test_trainNBO(self):
        listOPosts, listClasses = loadDataSet()
        myVocabList = createVocabList(listOPosts)
        trainMat = [] # list of lists, e.g., [[...], ..., [...]]
        for postinDoc in listOPosts:
            trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
        # this is interesting as the names sent to the funtion imply
        # different types than the names received by the function.
        # Compare sending trainCategory to receiving listClasses.
        # There isn't even a hint of meaning between those two names
        # at the program (self-referentiall) perspective.
        # p0Vect, p1Vect, pAbusive = trainNBO(trainMatrix, trainCategory)
        p0V, p1V, pAb = trainNBO(trainMat, listClasses)
        # print p0V, p1V, pAb
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()

