#!/usr/bin/env python

# pylint: disable=missing-docstring

import unittest
import sys

from numpy import *

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
        documents, classifications = bayes.load_documents()  # pylint: disable=unused-variable
        vocabulary = bayes.create_vocabulary(documents)
        features = bayes.bag_of_words_2_vec_mn(vocabulary, documents[0])
        expected = [
            0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1
        ]
        self.assertEqual(features, expected)

    def test_classify_nb(self):  # pylint: disable=missing-docstring
        documents = [
            ['stupid'],
            ['smart']
        ]
        classifications = [1, 0]
        vocabulary = bayes.create_vocabulary(documents)

        trainmat = []  # list of lists, e.g., [[...], ..., [...]]
        for document in documents:
            trainmat.append(bayes.set_of_words_2_vec(vocabulary, document))
        print "trainmat: ", trainmat, "\n"
        self.assertEqual(trainmat, [[1, 0], [0, 1]])
        p0_vec, p1_vec, p_abusive = bayes.train_nbo(trainmat, classifications)
        # print p0_vec, p1_vec, p_abusive

        this_doc = array(bayes.set_of_words_2_vec(vocabulary, ['smart']))
        print "this_doc: ", this_doc, "\n"
        result = bayes.classify_nb(this_doc, p0_vec, p1_vec, p_abusive)
        print "result: ", result, "\n"
        self.assertEqual(result, 0)

        this_doc = array(bayes.set_of_words_2_vec(vocabulary, ['stupid']))
        print "this_doc: ", this_doc, "\n"
        result = bayes.classify_nb(this_doc, p0_vec, p1_vec, p_abusive)
        print "result: ", result, "\n"
        self.assertEqual(result, 1)

        this_doc = array(bayes.set_of_words_2_vec(vocabulary, ['intelligent']))
        print "this_doc: ", this_doc, "\n"
        result = bayes.classify_nb(this_doc, p0_vec, p1_vec, p_abusive)
        print "result: ", result, "\n"
        self.assertEqual(result, 0)

    def test_create_vocabulary(self):
        documents = [
            ['stupid', 'garbage'],
            ['love', 'puppies']
        ]
        expected = ['stupid', 'garbage', 'love', 'puppies']
        word_list = bayes.create_vocabulary(documents)
        self.assertTrue(set(word_list) == set(expected))
        # don't want duplicate elements
        self.assertTrue(len(word_list) == len(expected))

    def test_train_nbo(self):
        listOPosts, listClasses = bayes.load_documents()
        myVocabList = bayes.create_vocabulary(listOPosts)
        trainmat = []  # list of lists, e.g., [[...], ..., [...]]
        for postindoc in listOPosts:
            trainmat.append(bayes.set_of_words_2_vec(myVocabList, postindoc))
        # this is interesting as the names sent to the funtion imply
        # different types than the names received by the function.
        # Compare sending trainCategory to receiving listClasses.
        # There isn't even a hint of meaning between those two names
        # at the program (self-referentiall) perspective.
        # p0Vect, p1Vect, pAbusive = trainNBO(trainMatrix, trainCategory)
        p0V, p1V, pAb = bayes.train_nbo(trainmat, listClasses)
        # print p0V, p1V, pAb
        self.assertAlmostEqual(pAb, 0.5)
        # self.assertTrue(False)

    def test_text_parse(self):
        big_string = "Big String.html.md - 733T"
        expected = ["big", "string", "html", "733t"]
        actual = bayes.text_parse(big_string)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
