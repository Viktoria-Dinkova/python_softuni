'''
По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да напишете програма,
с която ще разберете дали имате достатъчно време да изгледате епизода. По време на почивката отделяте време за обяд и време за отдих.
Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
Вход
От конзолата се четат 3 реда:
1.	Име на сериал – текст
2.	Продължителност на епизод  – цяло число в диапазона [10… 90]
3.	Продължителност на почивката  – цяло число в диапазона [10… 120]
Изход
На конзолата да се изпише един ред:
•	Ако времето е достатъчно да изгледате епизода:
"You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
•	Ако времето не Ви е достатъчно:
"You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
Времето да се закръгли до най-близкото цяло число нагоре.
'''

import math

ser_name = input()
episode_time = int(input())
chill_time = int(input())

lunch_time = chill_time / 8
rest_time = chill_time / 4

total_time = lunch_time + episode_time + rest_time

if (chill_time >= total_time):
    print(f'You have enough time to watch {ser_name} and left with {math.ceil(chill_time - total_time)} minutes free time.')

else:
    print(f"You don't have enough time to watch {ser_name}, you need {math.ceil(total_time - chill_time)} more minutes.")