#!/usr/bin/env python

import unittest
import sys
sys.path.append('../lib')
import bayes_literate as bayes

class TestNB(unittest.TestCase):
    def test_setOfWords2Vec(self):
        # listOPosts is actually...
        # listClasses is actually a list of labels for the data in listOPosts
        listOPosts, listClasses = bayes.load_data_set()
        myVocabList = bayes.create_vocabulary(listOPosts)
        features = bayes.setOfWords2Vec(myVocabList, listOPosts[0])
        expected = [
            0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1
        ]
        self.assertEqual(features, expected)

    # identical output to setOfWords
    # todo: find a way to test difference.
    def test_bagOfWords2VecMN(self):
        listOPosts, listClasses = bayes.load_data_set()
        myVocabList = bayes.create_vocabulary(listOPosts)
        features = bayes.bagOfWords2VecMN(myVocabList, listOPosts[0])
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
        word_list = bayes.create_vocabulary(dataSet)
        self.assertTrue(set(word_list) == set(expected))
        # don't want duplicate elements
        self.assertTrue(len(word_list) == len(expected))

    def test_trainNBO(self):
        listOPosts, listClasses = bayes.load_data_set()
        myVocabList = bayes.create_vocabulary(listOPosts)
        trainMat = [] # list of lists, e.g., [[...], ..., [...]]
        for postinDoc in listOPosts:
            trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))
        # this is interesting as the names sent to the funtion imply
        # different types than the names received by the function.
        # Compare sending trainCategory to receiving listClasses.
        # There isn't even a hint of meaning between those two names
        # at the program (self-referentiall) perspective.
        # p0Vect, p1Vect, pAbusive = trainNBO(trainMatrix, trainCategory)
        p0V, p1V, pAb = bayes.trainNBO(trainMat, listClasses)
        # print p0V, p1V, pAb
        self.assertAlmostEqual(pAb, 0.5)
        # self.assertTrue(False)

    def test_textParse(self):
        bigString = "Big String.html.md - 733T"
        expected = ["big", "string", "html", "733t"]
        actual = bayes.textParse(bigString)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
