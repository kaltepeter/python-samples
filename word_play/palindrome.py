#! /usr/bin/env python3

import scrabble
import string

longest = ""

for word in scrabble.wordlist:
    # if list(word) == list(reversed((word))) and len(word) > len(longest):
    if word == word[::-1] and len(word) > len(longest):
        longest = word

print(longest)
