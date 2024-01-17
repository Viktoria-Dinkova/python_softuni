# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# •	The weight of the snowball (integer).
# •	The time needed for the snowball to get to its target (integer).
# •	The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.
# Input
# •	On the first input line, you will receive N – the number of snowballs.
# •	On the next N*3 input lines, you will be receiving data about each snowball.
# Output
# •	You need to print the highest calculated snowball's value in the format:
# "{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"
# Constraints
# •	The number of snowballs (N) will be an integer in range [0, 100].
# •	The weight is an integer in the range [0, 1000].
# •	The time is an integer in the range [1, 500].
# •	The quality is an integer in the range [0, 100].

from math import floor

snowballs_number = int(input())
if not (0 <= snowballs_number <= 100):
    print('Wrong value - tray again:')
    snowballs_number = int(input())

snowball_value = 0
surch_weight = 0
surch_flays_time = 0
surch_quality = 0
surch_value = 0

for snowball in range(snowballs_number):

    weight = int(input())
    if not (0 <= weight <= 1000):
        print('Wrong value - tray again:')
        weight = int(input())
    flays_time = int(input())
    if not (1 <= flays_time <= 500):
        print('Wrong value - tray again:')
        flays_time = int(input())
    quality = int(input())
    if not (0 <= quality <= 100):
        print('Wrong value - tray again:')
        quality = int(input())

    snowball_value = (weight / flays_time) ** quality
    if snowball_value > surch_value:
        surch_weight = weight
        surch_flays_time = flays_time
        surch_quality = quality
        surch_value = snowball_value

print(f'{surch_weight} : {surch_flays_time} = {int(surch_value)} ({surch_quality})')
