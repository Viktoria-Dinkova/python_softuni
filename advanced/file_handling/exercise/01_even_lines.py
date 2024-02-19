"""
Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0.
Before you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.
"""

symbols = ["-", ",", ".", "!", "?"]

with open('texts/text.txt', "r") as text_in_file:
    text = text_in_file.readlines()

    for r in range(0, len(text), 2):
        for s in symbols:
            text[r] = text[r].replace(s, "@")

        print(*text[r].split()[::-1])
