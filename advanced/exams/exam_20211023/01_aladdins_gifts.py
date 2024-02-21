"""
First, you will receive a sequence of integers representing the materials for every wedding present. After that, you will be given another sequence of integers –
Genie magic level for every aim to make a gift.
Your task is to mix materials with magic levels so you can make presents, listed in the table below.
Gift	Magic needed
Gemstone	100 to 199
Porcelain Sculpture	200 to 299
Gold	300 to 399
Diamond Jewellery	400 to 499
To make a present, you should take the last integer of materials and sum it with the first magic level value. If the result is between or equal to the numbers described in the table above,
you make the corresponding gift and remove both materials and magic value. Otherwise:
•	If the product of the operation is under 100:
o	And if it is an even number, double the materials, and triple the magic, then sum it again.
o	And if it is an odd number, double the sum of the materials and the magic level. Then, check again if it is between or equal to any of the numbers in the table above.
•	If the product of the operation is more than 499, divide the sum of the material and the magic level by 2. Then, check again if it is between or equal to any of the numbers in the table above.
•	If, however, the result is not between or equal to any of the numbers in the table above after performing the calculation, remove both the materials and the magic level.
Stop crafting gifts when you are out of materials or magic level.
You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and a sculpture or gold and jewellery.
Input
•	The first line of input will represent the values of materials - integers, separated by a single space
•	On the second line, you will be given the magic levels - integers, separated by a single space
Output
•	On the first line - print whether you have succeeded in crafting the presents:
o	"The wedding presents are made!"
o	"Aladdin does not have enough wedding presents."
•	On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
o	"Materials left: {material1}, {material2}, …"
o	"Magic left: {magicValue1}, {magicValue2}, …
•	On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
"{present1}: {amount}
{present2}: {amount}
"""
from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

price_list = {
    'Gemstone': range(100, 200),
    'Porcelain Sculpture': range(200, 300),
    'Gold': range(300, 400),
    'Diamond Jewellery': range(400, 500)
}

presents = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while materials and magic:
    curr_material = materials.pop()
    curr_magic = magic.popleft()

    future_present = curr_material + curr_magic

    if future_present < 100:
        if future_present % 2 == 0:
            curr_material *= 2
            curr_magic *= 3
            future_present = curr_material + curr_magic
        else:
            future_present *= 2

        if future_present < 100:
            continue
        elif future_present >= 500:
            future_present //= 2

    elif future_present >= 500:
        future_present //= 2

    for k, v in price_list.items():
        if future_present in v:
            presents[k] += 1
            break

if (presents['Gemstone'] > 0 and presents['Porcelain Sculpture'] > 0) or (presents['Gold'] > 0 and presents['Diamond Jewellery'] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for pk, pv in presents.items():
    if pv > 0:
        print(f"{pk}: {pv}")