#!/usr/bin/env python3

from matplotlib import pyplot


data = open("life_expectancies_usa.txt", "r").readlines()
dates = []
male_life_expectancies = []
female_life_expectancies = []

for line in data:
    date, mle, fle = line.split(',')
    dates.append(date)
    male_life_expectancies.append(mle)
    female_life_expectancies.append(fle)

pyplot.plot(dates, male_life_expectancies, "bo-", label="Men")
pyplot.plot(dates, female_life_expectancies, "mo-", label="Women")
pyplot.legend(loc="upper left")
pyplot.ylabel("Age")
pyplot.xlabel("Year")
pyplot.title("Life expectancies for women and men in the USA over time")
pyplot.show()