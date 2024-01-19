# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move
# Find out who the winner is. If the first player wins, print "First player won".
# If the second player wins, print "Second player won". Otherwise, print "Draw!".

first_line = list(map(int, input().split()))
second_line = list(map(int, input().split()))
third_line = list(map(int, input().split()))

if ((first_line[0] == 1 and first_line[1] == 1 and first_line[2] == 1)
    or (second_line[0] == 1 and second_line[1] == 1 and second_line[2] == 1)
    or (third_line[0] == 1 and third_line[1] == 1 and third_line[2] == 1)

    or (first_line[0] == 1 and second_line[0] == 1 and third_line[0] == 1)
    or (first_line[1] == 1 and second_line[1] == 1 and third_line[1] == 1)
    or (first_line[2] == 1 and second_line[2] == 1 and third_line[2] == 1)

    or(first_line[0] == 1 and second_line[1] == 1 and third_line[2] == 1)
    or (first_line[2] == 1 and second_line[1] == 1 and third_line[0] == 1)):

    print('First player won')

elif ((first_line[0] == 2 and first_line[1] == 2 and first_line[2] == 2)
    or (second_line[0] == 2 and second_line[1] == 2 and second_line[2] == 2)
    or (third_line[0] == 2 and third_line[1] == 2 and third_line[2] == 2)

    or (first_line[0] == 2 and second_line[0] == 2 and third_line[0] == 2)
    or (first_line[1] == 2 and second_line[1] == 2 and third_line[1] == 2)
    or (first_line[2] == 2 and second_line[2] == 2 and third_line[2] == 2)

    or(first_line[0] == 2 and second_line[1] == 2 and third_line[2] == 2)
    or (first_line[2] == 2 and second_line[1] == 2 and third_line[0] == 2)):

    print('Second player won')

else:
    print('Draw!')

