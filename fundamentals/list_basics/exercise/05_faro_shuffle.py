# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of faro shuffles that should be made.
# Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.

input_string = input().split()
faros_count = int(input())

output_string = []
middle = int(len(input_string) / 2)

left_half = input_string[:middle]
right_half = input_string[middle:]

for _ in range(faros_count):
    output_string = []

    for card in range(middle):
        output_string.append(left_half[card])
        output_string.append(right_half[card])

    left_half = output_string[:middle]
    right_half = output_string[middle:]

print(f'{output_string}')