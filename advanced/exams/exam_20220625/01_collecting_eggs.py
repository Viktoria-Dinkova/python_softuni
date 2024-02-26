"""
On the first line, you will receive a sequence of numbers, each representing an egg with its size. On the second line,
you will receive another sequence of numbers, each representing a piece of paper with its size.
You should take the first egg and wrap it with the last piece of paper. Then, try to put it in a box with a size of 50.
Each wrapped-in-a-paper egg fills one box if it fits in it. Your task is to check whether you have filled at least one box.
You should comply with the following conditions:
•	If the egg is not fresh anymore (its size is less than or equal to 0), you need to remove it from the sequence before it is wrapped with a piece of paper.
•	If the sum of the egg's size and the paper's size is less than or equal to the box's size (50), put the wrapped egg in the box and remove both from the sequences.
o	Otherwise, you cannot fill a box, so remove both the egg and the paper from the sequences without putting them in a box.
•	During your work, you noticed that Old MacDonald is superstitious. If the size of an egg is 13 it brings bad luck to him.
You should remove this egg from the sequence before it is wrapped with a piece of paper.
o	Furthermore, each time you take an egg with a size of 13, it will be best to swap the first and last pieces of paper positions to bring the good luck back to Old MacDonald.
	Note: There will be NO case where there will be just one piece of paper left.
For more clarification see the examples below.
Input
•	In the first line, you will be given a sequence of eggs with their sizes - integers separated by comma and space ", " in the range [-100, 100]
•	In the second line, you will be given a sequence of pieces of paper with their sizes - integers separated by comma and space ", " in the range [1, 100]
"""
from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
paper = deque([int(y) for y in input().split(', ')])

count = 0

while eggs and paper:

    curr_egg = eggs.popleft()
    curr_paper = paper.pop()

    if curr_egg <= 0:
        paper.append(curr_paper)

    elif curr_egg == 13:
        first_paper = paper.popleft()
        paper.append(first_paper)
        paper.appendleft(curr_paper)

    else:
        curr_wrapped = curr_paper + curr_egg
        if curr_wrapped <= 50:
            count += 1

if count > 0:
    print(f"Great! You filled {count} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join(map(str, eggs))}')

if paper:
    print(f'Pieces of paper left: {", ".join(map(str, paper))}')
