# First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if any, and change their values to "None".
# •	"Required {gift} {index}"
# o	If the index is valid, replace the gift on the given index with the given gift.
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
# •	On the 1st line,  you will receive the names of the gifts, separated by a single space.
# •	On the following lines, until the "No Money" command is received, you will be receiving commands.
# •	The input will always be valid.
# Output
# •	Print the gifts in the format described above.

gifts = input().split()
message = input()

while message != 'No Money':
    message = message.split()

    if message[0] == 'OutOfStock':
        for i in range(len(gifts)-1,-1,-1):
            curr_gift = gifts[i]
            if curr_gift == message[1]:
                gifts[i] = 'None'

    if message[0] == 'Required':


        if 0 <= int(message[2]) < len(gifts):
            gifts[int(message[2])] = message[1]

    if message[0] == 'JustInCase':
        gifts.pop(-1)
        gifts.append(message[1])

    message = input()

for _ in range(gifts.count('None')):
    gifts.remove('None')

print(' '.join(gifts))