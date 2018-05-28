#!/usr/bin/env python3

from matplotlib import pyplot
import string

data = open("mystery.txt", encoding="utf-8").read()

letter_counts = {}
for char in string.ascii_lowercase:
    letter_counts[char] = 0

for char in data:
    char = char.lower()
    if char in string.ascii_lowercase:
        letter_counts[char] += 1

frequencies = letter_counts.items()
labels = []
counts = []
for letter, count in sorted(frequencies):
    labels.append(letter)
    counts.append(count)

xlocations = range(len(frequencies))
width = 0.5
pyplot.xticks([elt + width / 2 for elt in xlocations], labels)
pyplot.bar(xlocations, counts, width=width)

pyplot.xlabel("Letter")
pyplot.ylabel("Frequency")
pyplot.title("Letter frequencies in the US Constitution")
pyplot.show()
