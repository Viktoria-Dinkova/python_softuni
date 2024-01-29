# Write a program that reads a sequence of strings, separated by a single space.
# Each string should be repeated N times, where N is the length of the string.
# Print the final strings concatenated into one string.

sequence_of_string = input().split()
output_sequence = ''
for word in sequence_of_string:
    output_sequence += word * len(word)

print(f'{output_sequence}')