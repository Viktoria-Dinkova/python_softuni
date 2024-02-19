"""
Write a program that reads a text file, inserts line numbers in front of each line, and counts all the letters and punctuation marks.
The result should be written in another text file.
"""
from string import punctuation
import os

way = os.path.join('texts', 'text.txt')
way_out = os.path.join('texts', 'out_text2.txt')

with open(way, 'r') as file:
    text = file.readlines()

with open(way_out,'w') as out_file:

    for row in range(1, len(text)+1):
        row_text = text[row-1][:-1]
        letters, marks = 0, 0
        for symbol in row_text:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                marks += 1

        out_file.write(f"Line {row}: {row_text} ({letters})({marks})\n")

