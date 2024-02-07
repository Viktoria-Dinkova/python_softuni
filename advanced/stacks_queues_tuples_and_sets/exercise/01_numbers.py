'''
First, you will be given two sequences of integer values on different lines. The values of the sequences are separated by a single space between them.
Keep in mind that each sequence should contain only unique values.
Next, you will receive a number - N. On the following N lines, you will receive one of the following commands:
•	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
•	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
•	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
•	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
•	"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.
'''

first_line = set(int(x) for x in input().split())
second_line = set(int(x) for x in input().split())

for _ in range(int(input())):
    command, line, *sequence = input().split()

    action = command + ' ' + line
    sequence = set(int(s) for s in sequence)

    if action == 'Add First':
        first_line = first_line.union(sequence)
    elif action == 'Add Second':
        second_line = second_line.union(sequence)
    elif action == 'Remove First':
        first_line = first_line.difference(sequence)
    elif action == 'Remove Second':
        second_line = second_line.difference(sequence)
    elif action == 'Check Subset':
        print(first_line.issubset(second_line) or second_line.issubset(first_line))

print(*sorted(first_line), sep=', ')
print(*sorted(second_line), sep=', ')
