'''a slightly different implementation'''

import re

def tokenize(message): #  pylint: disable=missing-docstring
    message = message.lower()
    all_words = re.findall("[a-z0-9']+", message)
    return set(all_words)
