#!/usr/bin/env python

# pylint: disable=missing-docstring

# There has been a dog continuously yapping across
# the street, which is right outside my window, for the
# better part of 30 minutes. It's 4 am. For some reason,
# I have some syntax errors in this script, and I just
# can't seem to figure out what they are. I wonder why.

import glob
import re # pylint: disable=unused-import
import random
from collections import Counter
import sys
sys.path.append('./lib')
import naive_bayes_classifier as nbc # pylint: disable=import-error


def split_data(data, prob):
    """split data into fractions [prob, 1-prob]"""
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

def spamfinder():

    spampath = r"/Users/doolin/tmp/*/*"
    spamdata = []

    for files in glob.glob(spampath):
        is_spam = "ham" not in files

        with open(files, 'r') as spamfile:
            for line in spamfile:
                if line.startswith("Subject:"):
                    # remove the leading "Subject: " and keep what's left
                    subject = re.sub(r"^Subject: ", "", line).strip()
                    spamdata.append((subject, is_spam))

    # print spamdata

    random.seed(0) # get the same answer as the example in the book
    train_data, test_data = split_data(spamdata, 0.75)

    classifier = nbc.NaiveBayesClassifier()
    classifier.train(train_data)

    classified = [(subject, is_spam, classifier.classify(subject))
                  for subject, is_spam in test_data]

    counts = Counter((is_spam, spam_probability > 0.5)
                     for _, is_spam, spam_probability in classified)

    print counts

if __name__ == "__main__":
    spamfinder()
