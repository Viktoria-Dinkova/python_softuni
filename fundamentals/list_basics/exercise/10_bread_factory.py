# You have initial energy 100 and initial coins 100. You will be given a string representing the working day events. Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
# Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")
# •	If the event is "rest":
# o	You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100). Print: "You gained {gained_energy} energy.".
# o	After that, print your current energy: "Current energy: {current_energy}.".
# •	If the event is "order":
# o	You've earned some coins (the number in the second part).
# o	Each time you get an order, your energy decreases by 30 points.
# 	If you have the energy to complete the order, print: "You earned {earned} coins.".
# 	Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
# •	In any other case, you have an ingredient you should buy. The second part of the event contains the coins you should spend.
# o	If you have enough money, you should buy the ingredient and print:
# "You bought {ingredient}."
# o	Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
# If you managed to handle all events throughout the day, print on the following 3 lines:
# "Day completed!"
# "Coins: {coins}"
# "Energy: {energy}"
# Input / Constraints
# You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
# "event1|event2| … eventN".
# Each event contains an event name or an ingredient and a number, separated by a dash in the format: "{event/ingredient}-{number}"
# Output
# Print the corresponding messages described above.

input_string = input().split('|')
energy = 100
coins = 100

gained_energy = 0
earned_coins = 0
spend_coins = 0

for element in input_string:
    day_event = element.split('-')
    event = day_event[0]
    value = int(day_event[1])

    if event == "rest":
        gained_energy = value
        energy += gained_energy
        if energy >= 100:
            print(f'You gained 0 energy.')
            print(f'Current energy: 100.')
            energy = 100
        else:
            print(f'You gained {gained_energy} energy.')
            print(f'Current energy: {energy}.')
    elif event == "order":
        if energy >= 30:
            earned_coins = value
            coins += value
            energy -= 30
            print(f'You earned {earned_coins} coins.')
        else:
            energy += 50
            print(f'You had to rest!')

    else:
        if coins >= value:
            spend_coins = value
            coins -=value
            print(f'You bought {event}.')
        else:
            print(f'Closed! Cannot afford {event}.')
            break
else:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
