#!/usr/bin/env python

# pylint: disable=missing-docstring

# TODO: save copies of feeds to spec/fixtures, then comment
# out the feed acquisition.

import sys

import feedparser

sys.path.append('./lib')
import bayes_literate as bayes


newyork = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sanfran = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')

print len(newyork['entries'])
print len(sanfran['entries'])

# pylint: disable=invalid-name
def getTopWords(ny, sf):
    import operator
    vocabList, p0V, p1V = bayes.local_words(ny, sf)
    topNY = []
    topSF = []
    for i in range(len(p0V)):
        if p0V[i] > -6.0:
            topSF.append((vocabList[i], p0V[i]))
        if p1V[i] > -6.0:
            topSF.append((vocabList[i], p0V[i]))
    sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse=True)
    print "SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**"
    print sortedSF
    for item in sortedSF:
        print item[0]
    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
    print "NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**"
    print sortedNY
    for item in sortedNY:
        print item[0]

getTopWords(newyork, sanfran)
