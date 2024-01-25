# You have now returned from your world tour. On your way, you have discovered some new plants,
# and you want to gather some information about them and create an exhibition to see which plant is highest rated.
# On the first line, you will receive a number n. On the next n lines,
# you will be given some information about the plants that you have discovered in the format: "{plant}<->{rarity}".
# Store that information because you will need it later. If you receive a plant more than once, update its rarity.
# After that, until you receive the command "Exhibition", you will be given some of these commands:
# •	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# •	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# •	"Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given plant name is invalid, print "error"
# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The average rating should be formatted to the second decimal place.

number_of_plants = int(input())
plant_list = {}
for i in range(number_of_plants):
    info = input().split('<->')
    current_plent = info[0]
    rarity = int(info[1])
    plant_list[current_plent] = [rarity, []]

while True:
    command = input().split(': ')
    task = command[0]
    if task == 'Exhibition':
        print('Plants for the exhibition:')
        for k, v in plant_list.items():
            if len(v) > 1:
                avarage_rating = sum(v[1]) / len(v[1])
            else:
                avarage_rating = 0
            print(f'- {k}; Rarity: {v[0]}; Rating: {avarage_rating:.2f}')
        break
    elif task == 'Rate':
        task_info = command[1].split(' - ')
        plant = task_info[0]
        rating = float(task_info[1])
        if plant in plant_list.keys():
            plant_list[plant][1].append(rating)

    elif task == 'Update':
        task_info = command[1].split(' - ')
        plant = task_info[0]
        rear = int(task_info[1])
        if plant in plant_list.keys():
            plant_list[plant][0] = rear

    elif task == 'Reset':
        plant = command[1]
        if plant in plant_list.keys():
            del plant_list[plant][1]

