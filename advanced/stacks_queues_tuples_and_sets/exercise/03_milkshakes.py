'''
First, you will be given two sequences of integers representing chocolates and cups of milk.
You have to start with the last chocolate and try to match it with the first cup of milk. If their values are equal,
you should make a milkshake and remove both ingredients. Otherwise, you should move the cup of milk at the end of
the sequence and decrease the value of the chocolate by 5 without moving it from its position.
If any of the values are equal to or below 0, you should remove them from the records right before mixing them with the other ingredients.
When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need to stop making chocolate milkshakes.
Input
•	On the first line of input, you will receive the integers representing the chocolate, separated by  ", ".
•	On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
Output
•	On the first line, print:
o	If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
o	Otherwise: "Not enough milkshakes."
•	On the second line - print:
o	If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
o	Otherwise: "Chocolate: empty"
•	On the third line - print:
o	If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
o	Otherwise: "Milk: empty"

'''

from collections import deque

chocolate = deque(int(x) for x in input().split(', '))
milk = deque(int(x) for x in input().split(', '))
shakes = []

while chocolate and milk:
    if len(shakes) == 5:
        break

    curr_chocolate = chocolate.pop() if milk[0] or not chocolate[-1] else 0
    curr_milk = milk.popleft() if curr_chocolate or not milk[0] else 0

    if not curr_milk:
        continue

    if curr_chocolate == curr_milk:
        shakes.append(curr_chocolate)
    else:
        if curr_chocolate > 0:
            chocolate.append(curr_chocolate)
        if curr_milk > 0:
            milk.appendleft(curr_milk)
        if curr_milk > 0 and curr_chocolate > 0:
            curr_chocolate = chocolate.pop()
            curr_chocolate -= 5
            chocolate.append(curr_chocolate)

if len(shakes) == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolate:
    print('Chocolate: ', end='')
    print(*chocolate, sep=', ')
else:
    print('Chocolate: empty')

if milk:
    print('Milk: ', end='')
    print(*milk, sep=', ')
else:
    print('Milk: empty')