# Write a program, which keeps a dictionary with synonyms.
# The key of the dictionary will be the word. The value will be a list of all the synonyms of that word.
# You will be given a number n – the count of the words.
# After each term, you will be given a synonym, so the count of lines you should read from the console is 2 * n.
# You will be receiving a word and a synonym each on a separate line like this:
# •	{word}
# •	{synonym}
# If you get the same word twice, just add the new synonym to the list.
# Print the words in the following format:
# {word} - {synonym1, synonym2 … synonymN}

word_count = int(input())

syn_dictionary = {}

for _ in range(word_count):
    word = input()
    if word not in syn_dictionary:
        syn_dictionary[word] = input()
    else:
        syn_dictionary[word] += ', ' + input()

for key, value in syn_dictionary.items():
    print(f'{key} - {value}')