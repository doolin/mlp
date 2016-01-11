#!/usr/bin/env python

# pylint: disable=missing-docstring

# There has been a dog continuously yapping across
# the street, which is right outside my window, for the
# better part of 30 minutes. It's 4 am. For some reason,
# I have some syntax errors in this script, and I just
# can't seem to figure out what they are. I wonder why.

import glob
import re # pylint: disable=unused-import

def spamfinder():

    spampath = r"/Users/doolin/tmp/*/*"
    spamdata = []

    for files in glob.glob(spampath):
        print files
        is_spam = "ham" not in files

        with open(files, 'r') as spamfile:
            for line in spamfile:
                if line.startswith("Subject:"):
                    # remove the leading "Subject: " and keep what's left
                    subject = re.sub(r"^Subject: ", "", line).strip()
                    spamdata.append((subject, is_spam))


if __name__ == "__main__":
    spamfinder()
