# You need to categorize dragons by their type. For each dragon, identified by name, keep information about his stats (damage, health, and armor).
# Type is preserved as in the order of input, but dragons are sorted alphabetically by their name.
# For each type, you should also print the average damage, health, and armor of the dragons. For each dragon, print his own stats.
# There may be missing stats in the input, though. If a stat is missing you should assign it default values.
# Default values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked by "null".
# The input is in the following format "{type} {name} {damage} {health} {armor}".
# The "type" and the "name" are strings. The "damage", the "health", and the "armor" are integers.
# Any of the integers may be assigned "null" value. See the examples below for better understanding of your task.
# If the same dragon is added a second time, the new stats should overwrite the previous ones. Two dragons are considered equal if they match by both name and type.

number_of_drsgons = int(input())
dragons = {}

for i in range(number_of_drsgons):
    info = input().split()

    type = info[0]
    name = info[1]
    demage = int(info[2] if info[2] != 'null' else '45')
    health = int(info[3] if info[3] != 'null' else '250')
    armor = int(info[4] if info[4] != 'null' else '10')

    dragons[name] = {type: {'demage': demage, 'health': health, 'armor': armor}}

print(dragons)


