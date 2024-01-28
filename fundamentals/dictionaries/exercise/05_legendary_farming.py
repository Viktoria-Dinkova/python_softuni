# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# •	"Shadowmourne" - requires 250 Shards
# •	"Valanyr" - requires 250 Fragments
# •	"Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race.
# At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.
# # Input
# •	Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Output
# •	On the first line, print the obtained item in the format: "{Legendary item} obtained!"
# •	On the next three lines, print the remaining key materials
# •	On the several final lines, print the junk items
# •	All materials should be printed in the format: "{material}: {quantity}"
# •	The output should be lowercase, except for the first letter of the legendary
materials = {"shards": 0, "fragments": 0, "motes": 0}
is_legendary = False

while True:
    materials_in = input().split()

    for i in range(0, len(materials_in), 2):
        if materials_in[i + 1].lower() not in materials:
            materials[materials_in[i + 1].lower()] = int(materials_in[i])
        else:
            materials[materials_in[i + 1].lower()] += int(materials_in[i])

        if materials["shards"] >= 250:
            materials["shards"] -= 250
            legendary_item = 'Shadowmourne'
            is_legendary = True
        elif materials["fragments"] >= 250:
            materials["fragments"] -= 250
            legendary_item = 'Valanyr'
            is_legendary = True
        elif materials["motes"] >= 250:
            materials["motes"] -= 250
            legendary_item = 'Dragonwrath'
            is_legendary = True

        if is_legendary == True:
            break

    if is_legendary == True:
        print(f'{legendary_item} obtained!')
        for key, value in materials.items():
            print(f'{key}: {value}')
        break



