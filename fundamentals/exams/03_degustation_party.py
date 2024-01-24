# Create a program that keeps information about guests liked and disliked meals.
# You will be receiving lines with commands until you receive the "Stop" command. The possible commands are:
# •	"Like-{guest}-{meal}":
# o	Add the meal to the guest's collection of meals.
# o	If the guest does not exist, add them and their meal to your record.
# o	If the guest already has the meal in their collection, do not add it.
# •	"Dislike-{guest}-{meal}":
# o	Remove the meal of the guest’s collection of liked meals and print:
# "{Guest} doesn't like the {meal}."
# You must keep the count of unliked meals of all unliked meals!
# o	If the guest does not exist, print:
#  "{Guest} is not at the party."
# o	If the guest does not have the meal at the like list, print:
#  "{Guest} doesn't have the {meal} in his/her collection."
# In the end, you should print the guests with their liked meals. Then print the count of unliked meals in the format below:
# "{Guest1}: {meal1}, {meal2} ... {mealN}
# {Guest2}: {meal1}, {meal2} ... {mealN}
# …
# {GuestN}: {meal1}, {meal2} ... {mealN}
# Unliked meals: {count of all unliked meals}"
# Input
# •	You will be receiving lines until you receive the "Stop" command.
# •	The input will always be valid.
# Output
# •	Print the guests with their meals in the format described above.
# •	Print the count of unliked meals in the format described above.

like_list = {}
dislike_list = []

while True:
    info = input().split('-')
    command = info[0]

    if command == 'Stop':
        for k,v in like_list.items():
            print(f'{k}: {", ".join(v)}')
        print(f'Unliked meals: {len(dislike_list)}')
        break
    else:
        gest = info[1]
        meal = info[2]

        if command == 'Like':
            if gest not in like_list.keys():
                like_list[gest] = [meal]
            else:
                if meal not in like_list[gest]:
                    like_list[gest].append(meal)

        elif command == 'Dislike':

            if gest in like_list.keys():
                if meal in like_list[gest]:
                    like_list[gest].remove(meal)
                    dislike_list.append(meal)
                else:
                    print(f"{gest} doesn't have the {meal} in his/her collection.")
            else:
                print(f"{gest} is not at the party.")

            print(f"{gest} doesn't like the {meal}.")

