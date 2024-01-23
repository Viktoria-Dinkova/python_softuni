# You will receive a single input line containing strings, separated by spaces. The strings may contain any ASCII character except whitespace. Then you will begin receiving commands in one of the following formats:
# •	merge {startIndex} {endIndex}
# •	divide {index} {partitions}
# Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex. In other words, you should concatenate them.
# Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
# If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.
# Every time you receive the divide command, you must divide the element at the given index into several small substrings with equal length. The count of the substrings should be equal to the given partitions.
# Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
# If the string cannot be exactly divided into the given partitions, make all partitions except the last with equal lengths and make the last one - the longest.
# Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
# The input ends when you receive the command "3:1". At that point, you must print the resulting elements, joined by a space.
# Input
# •	The first input line will contain the array of data.
# •	On the next several input lines, you will receive commands in the format specified above.
# •	The input ends when you receive the command "3:1".
# Output
# •	As output, you must print a single line containing the elements of the array, joined by a space.

def merge(words: list, start: int, end: int) -> str:
    merged_text = ''

    if start < 0 or start > len(words) - 1:
        start = 0
    if end > len(words) - 1:
        end = len(words) - 1
    for substrings in range(start, end + 1):
        merged_text += words[substrings]

    words[start:end+1] = [merged_text]
    return (words)
def divided(word: str, partision_count: int) -> str:
    group_lenght = len(word) // partision_count
    words = []
    while len(word) >= group_lenght + 1:
        current_group = word[:group_lenght]
        word = word[group_lenght:]
        words.append(current_group)
    words.append(word)

    return (words)
def rethreat(array_of_data: list) -> str:
    command = ['start']
    while command[0] != '3:1':
        command = input().split()
        if command[0] == 'merge':
            array_of_data = merge(array_of_data, int(command[1]), int(command[2]))
        elif command[0] == 'divide':
            array_of_data[int(command[1])] = ' '.join(divided(array_of_data[int(command[1])],int(command[2]) ))
    print(' '.join(array_of_data))

rethreat(input().split())