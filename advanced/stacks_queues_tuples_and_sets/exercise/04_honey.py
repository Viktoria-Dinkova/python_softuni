'''
When a worker-bee has found enough nectar, she returns to the hive to drop off the load and pass the nectar
to waiting bees so they can really start the honey-making process.
You will receive 3 sequences:
•	a sequence of integers, representing working bees
•	a sequence of integers, representing nectar
•	a sequence of symbols – "+", "-", "*", or "/", representing the honey-making process.
Step one: check if a bee has collected enough nectar. You should take the first bee and try to match it with the last nectar:
•	If the nectar value is more or equal to the value of the bee, it is considered collected, and the bee returns to the hive to drop off the load (step two).
•	If the nectar value is less than the value of the bee, you should remove the nectar
and try to match the bee with the next nectar's value until the bee collects enough nectar.
Step two: When a bee successfully collects nectar, she returns to the hive, and you should calculate the honey made.
Take the first symbol in the sequence of symbols ("+", "-", "*" or "/") and make the corresponding calculation:
"{matched_bee} {symbol} {matched_nectar}"
The result represents the honey that is made from the passed nectar. The calculation should always return the absolute value of the result.
After the calculation, remove the bee, the nectar, and the symbol.
•	If the symbol is "/" and the nectar’s value is 0 (zero), skip the calculation and remove the bee, the nectar, and the symbol.
Stop making honey when you are out of bees or nectar.
'''
from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
honey_making_process = deque(input().split())

total_honey_made = 0

made_honey = {
    '+': lambda b, cn: b + cn,
    '-': lambda b, cn: b - cn,
    '*': lambda b, cn: b * cn,
    '/': lambda b, cn: b / cn,
            }
while working_bees and nectar:
    bee = working_bees.popleft()
    curr_nectar = nectar.pop()

    if curr_nectar < bee:
        working_bees.appendleft(bee)

    elif curr_nectar >= bee:
        operand = honey_making_process.popleft()
        if curr_nectar == 0 and operand == '/':
            continue
        else:
            total_honey_made += abs(made_honey[operand](bee, curr_nectar))

print(f'Total honey made: {total_honey_made}')
if working_bees:
    print('Bees left: ', end='')
    print(*working_bees, sep=', ')
elif nectar:
    print('Nectar left: ', end='')
    print(*nectar, sep=', ')