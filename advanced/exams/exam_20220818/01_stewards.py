"""
You will be given a sequence of 6 seats - every seat is a mix of a number and a letter in the format "{number}{letter}". You will also be given two more sequences of numbers only.
First, you have to take the first number of the first sequence and the last number of the second sequence. Next, take the sum of those two numbers and find its ASCII character.
•	Compare each of the two taken numbers and the found character with the seats. If you find a match, the passenger is seated, and the seat is considered taken. Remove both numbers from their sequences.
•	If there is no equality, the two numbers should be returned at the end of their sequences (first becomes last, last becomes first).
•	If you match an already taken seat, you should just remove both numbers from their sequences.
Each time you take numbers from the sequences and try to match them, you make one rotation. You should keep track of all rotations made.
The program should end under the following circumstances:
•	You have found 3 (three) seat matches
•	You have made a total of 10 rotations
Input
•	On the first line, you will be given a sequence of seats - strings separated by comma and space ", "
•	On the second and the third line, you will be given two more sequences - integers separated by a comma and a space ", "
Output
When the program ends, print the following on two different lines:
o	Seat matches: {matches separated by comma and space}
o	Rotations count: {total rotations made}
"""
from collections import deque

seats = input().split(', ')
first_sequence = deque(int(x) for x in input().split(", "))
second_sequence = deque(int(y) for y in input().split(", "))

matches = 0
rotations = 0
matches_seat = ''

while True:
    num_1 = first_sequence.popleft()
    num_2 = second_sequence.pop()
    asc_char = chr(num_1 + num_2)
    considered = [str(num_1)+asc_char, str(num_2)+asc_char]

    for consider in considered:

        if consider in seats:
            seats.remove(consider)
            matches_seat += consider + ', '
            matches += 1


    else:
        first_sequence.append(num_1)
        second_sequence.appendleft(num_2)

    rotations += 1

    if matches >= 3:
        break

    if rotations >= 10:
        break

print(f"Seat matches: {matches_seat[:-2]}")
print(f"Rotations count: {rotations}")
