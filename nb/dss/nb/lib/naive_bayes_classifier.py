# pylint: disable=missing-docstring

import sys
sys.path.append('../lib')
import nb

class NaiveBayesClassifier(object):

    def __init__(self, k=0.5):
        self.k = k
        self.word_probs = []

    def train(self, training_set):

        # count spam and non-spam messages
        num_spams = len([is_spam
                         for message, is_spam in training_set # pylint: disable=unused-variable
                         if is_spam])
        num_non_spams = len(training_set) - num_spams

        # run training data through our "pipeline"
        word_counts = nb.count_words(training_set)
        self.word_probs = nb.word_probabilities(word_counts,
                                                num_spams,
                                                num_non_spams,
                                                self.k)

    def classify(self, message):
        return nb.spam_probability(self.word_probs, message)
