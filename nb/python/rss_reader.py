#!/usr/bin/env python

# TODO: save copies of feeds to spec/fixtures, then comment
# out the feed acquisition.

import feedparser

ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')

print(len(ny['entries']))
print(len(sf['entries']))
