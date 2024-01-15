# Beaches are filled with sand, water, fish, and sun. Given a string,
# calculate how many times the words "Sand", "Water", "Fish", and "Sun"
# appear (case insensitive).

input_string = input()
key_words = ["sand", "water", "fish", "sun"]

counter = 0
start_index = 0
input_string= input_string.lower()

for word in key_words:
    if input_string.find(word) >= 0:
        counter += input_string.count(word)

print(f'{counter}')



