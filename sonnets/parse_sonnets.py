#!/usr/bin/env python3

import string

sonnets = open("sonnets.txt").readlines()
word_set = set([elt.strip() for elt in open("sowpods.txt")])
sonnet_words = set()


def strip_punctuation(word):
    # Remove surrounding punctuation. if apostrophe skip it
    word.replace("-", "")
    apostrophe_index = word.find("'")
    if apostrophe_index != -1:
        return None
    return word.strip(string.punctuation)


for line in sonnets:
    # split apart hyphenated words
    line_words = line.replace("-", " ").strip().split()

    # if empty line or sonnet number; skip
    if len(line_words) <= 1:
        continue

    for word in line_words:
        stripped = strip_punctuation(word)
        if stripped and len(stripped) > 1:
            sonnet_words.add(stripped.upper())

sonnet_words = list(sonnet_words)
sonnet_words.sort()

f = open("my_sonnet_words", "w")
for word in sonnet_words:
    f.write(word + "\n")

f.close()
