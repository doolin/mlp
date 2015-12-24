#!/usr/bin/env python

# pylint: disable=missing-docstring

import unittest
import sys

from numpy import *

sys.path.append('../lib')
import bayes_literate as bayes


class TestNB(unittest.TestCase):

    def test_set_of_words_2_vec(self):
        documents, classifications = bayes.load_documents()  # pylint: disable=unused-variable
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
        documents, classifications = bayes.load_documents()
        vocabulary = bayes.create_vocabulary(documents)
        trainmat = []  # list of lists, e.g., [[...], ..., [...]]
        for document in documents:
            trainmat.append(bayes.set_of_words_2_vec(vocabulary, document))
        # this is interesting as the names sent to the funtion imply
        # different types than the names received by the function.
        # Compare sending trainCategory to receiving classifications.
        # There isn't even a hint of meaning between those two names
        # at the program (self-referentiall) perspective.
        # p0Vect, p1Vect, pAbusive = trainNBO(trainMatrix, trainCategory)
        p0_vec, p1_vec, p_abusive = bayes.train_nbo(trainmat, classifications)
        # print p0V, p1V, pAb
        self.assertAlmostEqual(p_abusive, 0.5)
        # self.assertTrue(False)

    def test_text_parse(self):
        big_string = "Big String.html.md - 733T"
        expected = ["big", "string", "html", "733t"]
        actual = bayes.text_parse(big_string)
        self.assertEqual(expected, actual)

    def test_build_training_matrix(self):
        vocabulary = ['foo', 'bar', 'baz']
        documents = [
            ['foo', 'bar'],
            ['bar', 'baz']
        ]

        expected = [
            [1, 1, 0],
            [0, 1, 1]
        ]

        actual = bayes.build_training_matrix(vocabulary, documents)
        print "Actual training matrix: ", actual
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
