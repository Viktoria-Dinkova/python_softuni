# First, you will be given the level of fire inside the cell with the integer value of the cell,
# which represents the needed water to put out the fire.  They will be given in the following format:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
# Afterward you will receive the amount of water you have for putting out the fires.
# There is a range of fire for each fire type, and if a cell's value is below or exceeds it, it is invalid, and you do not need to put it out.
# Type of Fire	Range
# High	81 - 125
# Medium	51 - 80
# Low	1 - 50
# If a cell is valid, you should put it out by reducing the water with its value.
# Putting out fire also takes effort, and you need to calculate it. Its value is equal to 25% of the cell's value.
# In the end, you will have to print the total effort. Keep putting out cells until you run out of water.
# Skip it and try the next one if you do not have enough water to put out a given cell.
# In the end, print the cells you have put out in the following format:
# "Cells:
#  - {cell1}
#  - {cell2}
#  …
#  - {cellN}"
# "Effort: {effort}"
# The effort should be formatted to the second decimal place.

level_of_fire = input().split('#')
amount_of_water = int(input())

cells = []
effort = 0
total_fire = 0

for current_fire in level_of_fire:
    fire = current_fire.split(' = ')
    type_of_fire = fire[0]
    cell = int(fire[1])
    if amount_of_water < cell:
        continue
    if ((type_of_fire == 'High' and 81 <= cell <= 125) or (type_of_fire == 'Medium' and 51 <= cell <= 80) or (type_of_fire == 'Low' and 1 <= cell <= 50)):
        amount_of_water -= cell
        effort += cell * 0.25
        total_fire += cell
        cells.append(str(cell))
    else:
        continue

    if amount_of_water <= 0:
        break

print(f'Cells:')
for cell in cells:
    print(f' - {cell}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
