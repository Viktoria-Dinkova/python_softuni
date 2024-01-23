# Using comprehension, write a program that receives some text,
# separated by space, and take only those words whose length is even.
# Print each word on a new line.

print('\n'.join([word for word in input().split() if len(word) % 2 == 0]))