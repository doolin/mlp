#!/usr/bin/env python

'''
docstring
'''

from numpy import *  # pylint: disable=unused-wildcard-import, redefined-builtin, wildcard-import

'''
This example uses 0 and 1 for two different purposes.

1. Classifying a document as either good (0), or bad (1).
2. Indicating absence (0) or presence (1) of a feature (word)
   in a document.

This is somewhat confusing.
'''


def load_documents():
    '''hard-coded documents, should be in a test file, not in this file.'''
    documents = [
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classifications = [0, 1, 0, 1, 0, 1]  # 0 not abusive, 1 abusive
    return documents, classifications


def create_vocabulary(documents):
    '''creates vocabulary'''
    vocabulary = set([])
    for document in documents:
        vocabulary = vocabulary | set(document)
    return list(vocabulary)


def set_of_words_2_vec(vocabulary, document):
    '''
    vocabulary is the set of words, which are the features in this
    example. document is the list of words within in a document.

    What we do here is apply the labels 0 or 1 to a feature set
    corresponding to vocabulary word's absence or presence in the
    document.
    '''
    feature_labels = [0] * len(vocabulary)
    for word in document:
        if word in vocabulary:
            feature_labels[vocabulary.index(word)] = 1
        else:
            print "the word: %s is not in my vocabulary!" % word
    return feature_labels


def bag_of_words_2_vec_mn(vocabulary, input_set):
    ''' feature? '''
    feature_labels = [0] * len(vocabulary)
    for word in input_set:
        if word in vocabulary:
            feature_labels[vocabulary.index(word)] += 1
    return feature_labels


def train_nbo(train_matrix, classifications):
    ''' docstring '''
    # print "sum(train_matrix): ", sum(train_matrix)
    num_train_docs = len(train_matrix)
    num_words = len(train_matrix[0])
    # print "classifications: ", classifications
    # print "sum(classifications): ", sum(classifications)
    p_abusive = sum(classifications) / float(num_train_docs)
    p0_num = ones(num_words)
    p1_num = ones(num_words)
    # print "p0_num: ", p0_num
    p0_denom = 2.0
    p1_denom = 2.0

    for i in range(num_train_docs):
        if classifications[i] == 1:
            p1_num += train_matrix[i]
            p1_denom += sum(train_matrix)
        else:
            p0_num += train_matrix[i]
            p0_denom += sum(train_matrix)

    p1_vect = log(p1_num / p1_denom)  # pylint: disable=undefined-variable
    p0_vect = log(p0_num / p0_denom)  # pylint: disable=undefined-variable
    # print "p1_vect: ", p1_vect, "\n"
    # print "p0_vect: ", p0_vect, "\n"
    return p0_vect, p1_vect, p_abusive


def multiply(this_doc, p_vec):  # pylint: disable=missing-docstring
    return this_doc * p_vec


def compute_probability_spam(this_doc, p1_vec, p_class1):  # pylint: disable=missing-docstring
    return sum(multiply(this_doc, p1_vec)) + log(p_class1)  # pylint: disable=undefined-variable


def compute_probability_notspam(this_doc, p0_vec, p_class1):  # pylint: disable=missing-docstring
    return sum(multiply(this_doc, p0_vec)) + log(1.0 - p_class1)  # pylint: disable=undefined-variable


def classify_nb(this_doc, p0_vec, p1_vec, p_class1):
    ''' docstring'''
    p_spam = compute_probability_spam(this_doc, p1_vec, p_class1)
    p_notspam = compute_probability_notspam(this_doc, p0_vec, p_class1)
    # print "p_spam: ", p_spam, "\n"
    # print "p_notspam: ", p_notspam, "\n"
    if p_spam > p_notspam:
        return 1
    else:
        return 0

def build_training_matrix(vocabulary, documents, labeler):
    '''extracted from test case
       labeler is indicates presence or absence of a word
       in the vocabulary'''
    train_mat = []
    for document in documents:
        train_mat.append(labeler(vocabulary, document))
    return train_mat

def testing_nb():
    ''' docstring '''
    documents, classifications = load_documents()
    vocabulary = create_vocabulary(documents)
    train_mat = build_training_matrix(vocabulary, documents, set_of_words_2_vec)

    p0_vector, p1_vector, p_abusive = train_nbo(train_mat, classifications)
    print "p0_vector: ", p0_vector, " length: ", len(p0_vector), "\n"
    print "p1_vector: ", p1_vector, " length: ", len(p1_vector), "\n"
    print "pAb: ", p_abusive, "\n"
    test_entry = ['love', 'my', 'dalmation']
    this_doc = array(set_of_words_2_vec(vocabulary, test_entry))
    print "this_doc", this_doc, "length: ", len(this_doc), "\n"
    print test_entry, 'classifed as: ', classify_nb(this_doc, p0_vector, p1_vector, p_abusive)
    test_entry = ['stupid', 'garbage']
    this_doc = array(set_of_words_2_vec(vocabulary, test_entry))
    print test_entry, 'classifed as: ', classify_nb(this_doc, p0_vector, p1_vector, p_abusive)


def calc_most_freq(vocabulary, full_text):
    '''docstring'''
    import operator
    freq_dict = {}
    for token in vocabulary:
        freq_dict[token] = full_text.count(token)
    sorted_freq = sorted(freq_dict.iteritems(),
                         key=operator.itemgetter(1), reverse=True)
    return sorted_freq[:30]


def text_parse(big_string):
    '''docstring'''
    import re
    list_of_tokens = re.split(r'\W*', big_string)
    return [tok.lower() for tok in list_of_tokens if len(tok) > 2]


def spam_test():
    '''docstring'''
    documents = []
    classifications = []
    full_text = []

    # for i in range(1, 26):
    for i in range(1, 5):
        word_list = text_parse(open('lib/spam/%d.txt' % i).read())
        documents.append(word_list)
        full_text.extend(word_list)
        classifications.append(1)

        word_list = text_parse(open('lib/ham/%d.txt' % i).read())
        documents.append(word_list)
        full_text.extend(word_list)
        classifications.append(0)

    vocabulary = create_vocabulary(documents)

    # training_set = range(50); test_set = []
    # training_set = range(10); test_set = []
    training_set = range(5)
    test_set = []
    # for i in range(10):
    for i in range(3):
        rand_index = int(random.uniform(0, len(training_set)))
        test_set.append(training_set[rand_index])
        del training_set[rand_index]
    train_mat = []
    train_classes = []
    for doc_index in training_set:
        train_mat.append(set_of_words_2_vec(vocabulary, documents[doc_index]))
        train_classes.append(classifications[doc_index])
    p0_vector, p1_vector, p_spam = train_nbo(
        array(train_mat), array(train_classes))

    error_count = 0
    for doc_index in test_set:
        word_vector = set_of_words_2_vec(vocabulary, documents[doc_index])
        if classify_nb(array(word_vector), p0_vector, p1_vector, p_spam) != classifications[doc_index]:
            error_count += 1
    print "the error rate is: ", float(error_count) / len(test_set)


def local_words(feed1, feed0):
    ''' docstring '''
    import feedparser
    doc_list = []
    classifications = []
    full_text = []
    # min_len = min(len(feed['entries']), len(feed0['entries']))
    min_len = min(len(feed1['entries']), len(feed0['entries']))
    for i in range(min_len):
        word_list = text_parse(feed1['entries'][i]['summary'])
        doc_list.append(word_list)
        full_text.extend(word_list)
        classifications.append(1)

        word_list = text_parse(feed0['entries'][i]['summary'])
        doc_list.append(word_list)
        full_text.extend(word_list)
        classifications.append(0)

    vocabulary = create_vocabulary(doc_list)

    top_30_words = calc_most_freq(vocabulary, full_text)

    for pair_w in top_30_words:
        if pair_w[0] in vocabulary:
            vocabulary.remove(pair_w[0])
    training_set = range(2 * min_len)
    test_set = []

    for i in range(20):
        rand_index = int(random.uniform(0, len(training_set)))
        test_set.append(training_set[rand_index])
        del training_set[rand_index]
    train_mat = []
    train_classes = []

    for doc_index in training_set:
        train_mat.append(bag_of_words_2_vec_mn(
            vocabulary, doc_list[doc_index]))
        train_classes.append(classifications[doc_index])
    p0_vector, p1_vector, p_spam = train_nbo(
        array(train_mat), array(train_classes))

    error_count = 0
    for doc_index in test_set:
        word_vector = bag_of_words_2_vec_mn(vocabulary, doc_list[doc_index])
        if classify_nb(array(word_vector), p0_vector, p1_vector, p_spam) != \
                classifications[doc_index]:
            error_count += 1
    print 'the error rate is: ', float(error_count) / len(test_set)
    return vocabulary, p0_vector, p1_vector
