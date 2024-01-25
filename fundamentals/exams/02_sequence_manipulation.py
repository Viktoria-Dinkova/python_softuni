# You are given numbers in a sequence on a single line, separated by a space.
# After that, you will receive commands that modify the sequence differently:
# • "Add {value}" - you should add the given value to the end of the sequence.
# • "Remove {value}" - you should remove the first occurrence of the given value if there is such.
# • "Replace {value} {replacement}" - you should replace the first occurrence of the given value with the replacement if there is such occurrence.
# • "Collapse {value}" you must remove each number with a value less than the given one.
# When you receive the command "Finish", you should print the modified sequence and end the program.
# Input / Constraints • On the first line, you will receive a sequence with numbers, separated by spaces - integers in the range  [-1000...1000].
# • On the following lines, you will receive commands until the "Finish" command is received.
# • The commands will always be valid. Output • Print a single line the array of numbers separated by a space,
# with the modified valu

in_sequence = list(map(int, input().split()))
out_sequence = in_sequence
while True:
    command = input().split()

    if command[0] == 'Add':
        out_sequence.append(int(command[1]))
    elif command[0] == 'Remove' and int(command[1]) in out_sequence:
        out_sequence.remove(int(command[1]))
    elif command[0] == 'Replace' and int(command[1]) in out_sequence:
        index = out_sequence.index(int(command[1]))
        out_sequence.remove(int(command[1]))
        out_sequence.insert(index, int(command[2]))
    elif command[0] == 'Collapse':
        for num in out_sequence[::-1]:
            if num < int(command[1]):
                out_sequence.remove(num)
    if command[0] == 'Finish':
        out_sequence = list(map(str, out_sequence))
        print(f'{" ".join(out_sequence)}')
        break