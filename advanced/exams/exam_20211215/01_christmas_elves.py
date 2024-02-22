"""
The Christmas elves have special toy-making skills - еach elf can make a toy from a given number of materials.
First, you will receive a sequence of integers representing each elf's energy. On the following line, you will be given another sequence of integers,
each representing a number of materials in a box.
Your task is to calculate the total elves' energy used for making toys and the total number of successfully made toys.
You are very clever and have immediately recognized the pros and cons of the work process - the first elf takes the last box of materials and tries to create the toy:
•	Usually, the elf needs energy equal to the number of materials. If he has enough energy, he makes the toy. His energy decreases by the used energy, and the toy goes straight to Santa's bag.
Then, the elf eats a cookie reward which increases his energy by 1, and goes to the end of the line, preparing for the upcoming boxes.
•	Every third time one of the elves takes a box, he tries his best to be creative, and he will need twice as much energy as usual. If he has enough, he manages to create 2 toys.
Then, his energy decreases; he eats a cookie reward and goes to the end of the line, similar to the first bullet.
•	Every fifth time one of the elves takes a box, he is a little clumsy and somehow manages to break the toy when he just made it (if he made it).
The toy is thrown away, and the elf doesn't get a cookie reward. However, his energy is already spent, and it needs to be added to the total elves' energy.
o	If an elf creates 2 toys, but he is clumsy, he breaks them.
•	If an elf does not have enough energy, he leaves the box of materials to the next elf. Instead of making the toy,
the elf drinks a hot chocolate which doubles his energy, and goes to the end of the line, preparing for the upcoming boxes.
Note: North Pole's social policy is very tolerant of the elves. If the current elf's energy is less than 5 units, he does NOT TAKE a box, but he takes a day off. Remove the elf from the collection.
Stop crafting toys when you are out of materials or elves.
Input
•	The first line of input will represent each elf's energy - integers, separated by a single space
•	On the second line, you will be given the number of materials in each box - integers, separated by a single space
Output
•	On the first line, print the number of created toys: "Toys: {total_number_of_toys}"
•	On the second line, print the total used energy: "Energy: {total_used_energy}"
•	On the next two lines print the elves and boxes that are left, if there are any, otherwise skip the line:
o	"Elves left: {elf1}, {elf2}, … {elfN}"
o	"Boxes left: {box1}, {box2}, … {boxN}"
"""
from collections import deque

energy = deque(int(x) for x in input().split())
materials = deque(int(x) for x in input().split())

toys = 0
turn = 0
all_energy = 0

while True:
    curr_energy = energy.popleft()
    if curr_energy < 5:
        continue

    curr_material = materials.pop()

    turn += 1
    if turn % 3 == 0:
        if curr_energy >= curr_material * 2:
            toys += 2
            all_energy += (curr_material * 2)
            curr_energy -= (curr_material * 2)
            curr_energy += 1
        else:
            curr_energy *= 2
            materials.append(curr_material)

    elif turn % 5 == 0:
        toys -= 1
        all_energy += curr_energy
        if turn % 3 == 0:
            toys -= 1

    else:
        if curr_energy >= curr_material:
            toys += 1
            all_energy += curr_material
            curr_energy -= curr_material
            curr_energy += 1
        else:
            curr_energy *= 2
            materials.append(curr_material)

    if turn % 5 != 0:
        energy.append(curr_energy)

    if not energy or not materials:
        break

print(f'Toys: {toys}')
print(f'Energy: {all_energy}')

if energy:
    print(f"Elves left: {', '.join(map(str, energy))}")
if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")