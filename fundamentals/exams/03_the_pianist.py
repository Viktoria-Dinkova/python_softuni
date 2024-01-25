# You are a pianist, and you like to keep a list of your favorite piano pieces. Create a program to help you organize it
# and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have.
# On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:
# •	"Add|{piece}|{composer}|{key}":
# o	You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
# o	If the piece is already in the collection, print:
# "{piece} is already in the collection!"
# •	"Remove|{piece}":
# o	If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# •	"ChangeKey|{piece}|{new key}":
# o	If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"
# Input/Constraints
# •	You will receive a single integer at first – the initial number of pieces in the collection.
# •	For each piece, you will receive a single line of text with information about it.
# •	Then you will receive multiple commands in the way described above until the command "Stop".
# Output
# •	All the output messages with the appropriate formats are described in the problem description.

count_of_the_pieces = int(input())
piano_list = {}
for i in range(count_of_the_pieces):
    info = input().split('|')
    piece, composer, key = info
    piano_list[piece] = [composer, key]

while True:
    command = input().split('|')
    if command[0] == 'Stop':
        for k,v in piano_list.items():
            print(f'{k} -> Composer: {v[0]}, Key: {v[1]}')
        break

    elif command[0] == 'Add':
        creation, author, sort = command[1:]
        if creation in piano_list.keys():
            print(f'{creation} is already in the collection!')
        else:
            piano_list[creation] = [author, sort]
            print(f'{creation} by {author} in {sort} added to the collection!')

    elif command[0] == 'Remove':
        creation = command[1]
        # piano_list.popitem(creation, f'Invalid operation! {creation} does not exist in the collection.')
        if creation not in piano_list.keys():
            print(f'Invalid operation! {creation} does not exist in the collection.')
        else:
            del piano_list[creation]
            print(f'Successfully removed {creation}!')

    elif command[0] == 'ChangeKey':
        creation, sort = command[1:]
        if creation not in piano_list.keys():
            print(f'Invalid operation! {creation} does not exist in the collection.')
        else:
            piano_list[creation][1] = sort
            print(f'Changed the key of {creation} to {sort}!')
