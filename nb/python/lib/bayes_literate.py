#!/usr/bin/env python

from numpy import *


def load_documents():
    documents = [
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    labels = [0, 1, 0, 1, 0, 1]  # labels: 0 not abusive, 1 abusive
    return documents, labels


def create_vocabulary(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabulary, document):
    returnVec = [0] * len(vocabulary)
    for word in document:
        if word in vocabulary:
            returnVec[vocabulary.index(word)] = 1
        else:
            print "the word: %s is not in my vocabulary!" % word
    return returnVec


def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


def trainNBO(trainMatrix, trainCategory):
    print "sum(trainMatrix): ", sum(trainMatrix)
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    print "trainCategory: ", trainCategory
    print "sum(trainCategory): ", sum(trainCategory)
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    print "p0Num: ", p0Num
    p0Denom = 2.0
    p1Denom = 2.0
    print "range(numTrainDocs: ", range(numTrainDocs), "\n"
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix)
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix)
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    print "p1Vec: ", p1Vect, "\n"
    print "p0Vec: ", p0Vect, "\n"
    return p0Vect, p1Vect, pAbusive


def classifyNB(test_vector, p0Vec, p1Vec, pClass1):
    p1 = sum(test_vector * p1Vec) + log(pClass1)
    p0 = sum(test_vector * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    documents, labels = load_documents()
    vocabulary = create_vocabulary(documents)
    trainMat = []
    for document in documents:
        trainMat.append(setOfWords2Vec(vocabulary, document))
    p0V, p1V, pAb = trainNBO(trainMat, labels)
    print "p0V: ", p0V, "\n"
    print "p1V: ", p1V, "\n"
    print "pAb: ", pAb, "\n"
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(vocabulary, testEntry))
    print testEntry, 'classifed as: ', classifyNB(thisDoc, p0V, p1V, pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(vocabulary, testEntry))
    print testEntry, 'classifed as: ', classifyNB(thisDoc, p0V, p1V, pAb)


def calcMostFreq(vocabList, fullText):
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token] = fullText.count(token)
    sortedFreq = sorted(freqDict.iteritems(),
                        key=operator.itemgetter(1), reverse=True)
    return sortedFreq[:30]


def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def spamTest():
    docList = []
    classList = []
    fullText = []
    # for i in range(1, 26):
    for i in range(1, 5):
        wordList = textParse(open('lib/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('lib/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = create_vocabulary(docList)
    # trainingSet = range(50); testSet = []
    # trainingSet = range(10); testSet = []
    trainingSet = range(5)
    testSet = []
    # for i in range(10):
    for i in range(3):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNBO(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print "the error rate is: ", float(errorCount) / len(testSet)


def calcMostFreq(vocabList, fullText):
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token] = fullText.count(token)
    sortedFreq = sorted(freqDict.iteritems(),
                        key=operator.itemgetter(1), reverse=True)
    return sortedFreq[:30]


def localWords(feed1, feed0):
    import feedparser
    docList = []
    classList = []
    fullText = []
    minLen = min(len(feed['entries']), len(feed0['entries']))
    for i in range(minlen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    top30Words = calcMostFreq(vocabList, fullText)
    for pairW in top30Words:
        if pairW[0] in vocabList:
            vocabList.remove(pairW[0])
    trainingSet = range(2 * minLen)
    testSet = []
    for i in range(20):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != \
                classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ', float(errorCount) / len(testSet)
    return vocabList, p0V, p1V
