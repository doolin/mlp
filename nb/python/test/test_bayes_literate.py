#!/usr/bin/env python

import unittest
import sys
sys.path.append('../lib')
import bayes_literate as bayes

class TestNB(unittest.TestCase):
    def test_set_of_words_2_vec(self):
        # listOPosts is actually...
        # listClasses is actually a list of labels for the data in listOPosts
        documents, labels = bayes.load_documents()
        vocabulary = bayes.create_vocabulary(documents)
        features = bayes.set_of_words_2_vec(vocabulary, documents[0])
        expected = [
            0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1
        ]
        self.assertEqual(features, expected)

    # identical output to setOfWords
    # todo: find a way to test difference.
    def test_bag_of_words_2_vec_mn(self):
        listOPosts, listClasses = bayes.load_documents()
        myVocabList = bayes.create_vocabulary(listOPosts)
        features = bayes.bag_of_words_2_vec_mn(myVocabList, listOPosts[0])
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
        listOPosts, listClasses = bayes.load_documents()
        myVocabList = bayes.create_vocabulary(listOPosts)
        trainMat = [] # list of lists, e.g., [[...], ..., [...]]
        for postinDoc in listOPosts:
            trainMat.append(bayes.set_of_words_2_vec(myVocabList, postinDoc))
        # this is interesting as the names sent to the funtion imply
        # different types than the names received by the function.
        # Compare sending trainCategory to receiving listClasses.
        # There isn't even a hint of meaning between those two names
        # at the program (self-referentiall) perspective.
        # p0Vect, p1Vect, pAbusive = trainNBO(trainMatrix, trainCategory)
        p0V, p1V, pAb = bayes.train_nbo(trainMat, listClasses)
        # print p0V, p1V, pAb
        self.assertAlmostEqual(pAb, 0.5)
        # self.assertTrue(False)

    def test_text_parse(self):
        bigString = "Big String.html.md - 733T"
        expected = ["big", "string", "html", "733t"]
        actual = bayes.text_parse(bigString)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
