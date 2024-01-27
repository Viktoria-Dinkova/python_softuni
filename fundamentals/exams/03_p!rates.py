# Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate captain by the name of Jack Daniels.
# Together with your comrades Jim (Beam) and Johnny (Walker), you have been roaming the seas, looking for gold and treasure…
# and the occasional killing, of course. Go ahead, target some wealthy settlements and show them the pirate's way!
# Until the "Sail" command is given, you will be receiving:
# •	You and your crew have targeted cities, with their population and gold, separated by "||".
# •	If you receive a city that has already been received, you have to increase the population and gold with the given values.
# After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given.
# Events will be in the following format:
# •	"Plunder=>{town}=>{people}=>{gold}"
# o	You have successfully attacked and plundered the town, killing the given number of people and stealing the respective amount of gold.
# o	For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
# o	If any of those two values (population or gold) reaches zero, the town is disbanded.
# •	You need to remove it from your collection of targeted cities and print the following message: "{town} has been wiped off the map!"
# o	There will be no case of receiving more people or gold than there is in the city.
# •	"Prosper=>{town}=>{gold}"
# o	There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
# o	The gold amount can be a negative number, so be careful. If a negative amount of gold is given, print: "Gold added cannot be a negative number!" and ignore the command.
# o	If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the following message:
# "{gold added} gold added to the city treasury. {town} now has {total gold} gold."
# Input
# •	On the first lines, until the "Sail" command, you will be receiving strings representing the cities with their gold and population, separated by "||".
# •	On the following lines, until the "End" command, you will be receiving strings representing the actions described above, separated by "=>".
# Output
# •	After receiving the "End" command, if there are any existing settlements on your list of targets, you need to print all of them, in the following format:
# "Ahoy, Captain! There are {count} wealthy settlements to go to:
# {town1} -> Population: {people} citizens, Gold: {gold} kg
# {town2} -> Population: {people} citizens, Gold: {gold} kg
#    …
# {town…n} -> Population: {people} citizens, Gold: {gold} kg"
# •	If there are no settlements left to plunder, print:
# "Ahoy, Captain! All targets have been plundered and destroyed!"

cities = {}

while True:
    command = input().split('||')
    # Tortuga||345000||1250
    city = command[0]
    if city == 'Sail':
        break
    population, gold = int(command[1]), int(command[2])
    if city in cities.keys():
        cities[city][0] += population
        cities[city][1] += gold
    else:
        cities[city] = [population, gold]

while True:
    event = input().split('=>')
    # Plunder=>Tortuga=>75000=>380
    task = event[0]
    if task == 'End':
        if len(cities) > 0:
            print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
            for k,v in cities.items():
                print(f'{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg')
        else:
            print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
        break
    elif task == 'Plunder':
        town, people, money = event[1], int(event[2]), int(event[3])
        if cities[town][0] >= people and cities[town][1] >= money:
            print(f'{town} plundered! {money} gold stolen, {people} citizens killed.')
            cities[town][0] -= people
            cities[town][1] -= money
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            del cities[town]
            print(f'{town} has been wiped off the map!')

    elif task == 'Prosper':
        town, money = event[1], int(event[2])
        if money < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            cities[town][1] += money
            print(f'{money} gold added to the city treasury. {town} now has {cities[town][1]} gold.')


