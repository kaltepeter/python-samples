#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("SELECT text, answer, value FROM clue LIMIT 10")
results = cursor.fetchall()

for clue in results:
    # text = clue[0].encode('utf-8')
    # answer = clue[1]
    # value = clue[2]
    text, answer, value = clue
    text = text.encode('utf-8')

    print("[$%s]" % (value,))
    print("Question: %s" % (text,))
    print("Answer: What is '%s'?" % (answer,))
    print("")

connection.close()
