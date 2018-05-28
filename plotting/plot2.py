#!/usr/bin/env python3

from matplotlib import pyplot
import random

x_values = [0, 4, 7, 20, 22, 25]
y_values = [random.randint(0, 30) for elt in x_values]
pyplot.plot(x_values, y_values, "o-")

pyplot.ylabel("Values")
pyplot.xlabel("Time")
pyplot.title("Test Plot")
pyplot.show()