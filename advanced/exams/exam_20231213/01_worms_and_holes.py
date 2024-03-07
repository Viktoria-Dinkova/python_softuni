'''
The first line will give you a sequence of integers representing worms. Afterwards, you will be given another sequence of integers representing holes.
You have to start with the last worm and try to match it with the first hole.
•	If their values are equal, the worm fits the hole and can get into it. After that, you should remove both of them from their sequences.
Otherwise, you should remove the hole and decrease the value of the worm by 3.
•	If the worm value becomes equal to or below 0, remove it from the sequence before trying to match it with the hole.
You need to stop matching when you have no more worms or holes.
Input / Constraints
•	On the first line, you will receive the integers, representing the worm size, separated by a single space.
•	On the second line, you will receive the integers, representing the hole size, separated by a single space.
•	All given numbers will be valid integers in the range [1, 50].
Output
•	On the first line:
	If there are matches print the following:
o	"Matches: {matchesCount}"
	If there are no matches print the following:
o	"There are no matches."
•	On the second line print:
	If there are no worms left and all of them fit a hole:
o	"Every worm found a suitable hole!"
	If there are no worms left but only some of them fit a hole:
o	"Worms left: none"
	If there are worms left:
o	"Worms left: {worm1}, {worm2}, (…),{wormn}"
•	On the third line print:
	If there are no holes left:
o	"Holes left: none"
	If there are holes left:
o	"Holes left: {hole1}, {hole2}, (…),{holen}"
'''
from collections import deque

worms = [int(w) for w in input().split()]
holes = deque(int(h) for h in input().split())

matches = 0
removed_holes = 0

while worms or holes:
    if worms[-1] == holes[0]:
        matches += 1
        removed_holes += 1
        worms.pop()
        holes.popleft()
        if not worms or not holes:
            break

    else:
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

        holes.popleft()
        removed_holes += 1
        if not worms or not holes:
            break


if matches > 0:
    print(f'Matches: {matches}')
else:
    print(f'There are no matches.')

if not worms:
    if matches == removed_holes:
        print('Every worm found a suitable hole!')
    else:
        print(f'Worms left: none')
else:
    print(f'Worms left: {", ".join(map(str, worms))}')

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(map(str, holes))}")
