"""
You will have to keep information for all the conquered peaks if any.
Every day, Alex will use one portion of his daily food supplies and will exhaust one of his daily stamina.
First, you will be given a sequence of numbers, representing the quantities of the daily portions of food supplies in his backpack.
Afterward, you will be given another sequence of numbers, representing the quantities of the daily stamina he will have at his disposal for the next seven days.
You have to sum the quantity of the last daily food portion with the quantity of the first daily stamina. He will start climbing from the first peak in the table below to the last one.
•	If the sum is equal to or greater than the corresponding Mountain Peak’s Difficulty level from the table below, it means that the peak is conquered.
 In this case, you should remove both quantities from the sequences and continue with the next ones towards the next peak.
•	If the sum is less than the corresponding Mountain Peak’s Difficulty level from the table below, the peak remains unconquered.
You should remove both quantities from the sequences. Alex will have to sleep in his tent. On the next day, he will try the same peak once again.

Mountain Peaks	Difficulty level
Vihren	80
Kutelo	90
Banski Suhodol	100
Polezhan	60
Kamenitza	70

Alex will try to conquer as many peaks as he can in seven days. If he manages to climb all the peaks, the journey ends and the output is printed on the Console.
Finally, print on the Console all the conquered peaks(in the order of climbing).
Input
•	On the first line, you will receive the food portions, separated by a comma and a single space (', ').
•	On the second line, you will receive the stamina, separated by a comma and a single space (', ').
Output
•	On the first line – print whether Alex managed to reach his goal and climb all the peaks in his list:
o	If he managed to conquer all: "Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK"
o	If he didn't manage to climb all of the peaks: "Alex failed! He has to organize his journey better next time -> @PIRINWINS"
•	Then, in either case, you need to print all the conquered peaks (in the order of climbing) if any:
"Conquered peaks:
{peak1}
{peak2}
…
{peakn}"
o	If there are no concurred peaks, do NOT print this message.

"""
from collections import deque

food_portions = [int(fp) for fp in input().split(', ')]
stamina = deque(int(fp) for fp in input().split(', '))

peaks = deque([('Vihren',	80), ('Kutelo',	90), ('Banski Suhodol', 100), ('Polezhan', 60), ('Kamenitza', 70)])

power = 0
conquered = []

for day in range(1, 8):

    dayly_portion = food_portions.pop()
    dayly_stamina = stamina.popleft()
    power = dayly_portion + dayly_stamina
    peak_per_day = peaks.popleft()

    if power >= peak_per_day[1]:
        conquered.append(peak_per_day[0])
        if not peaks:
            print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
            break

    else:
        peaks.appendleft(peak_per_day)

    if not food_portions or not stamina:
        print( "Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

else:
    print( "Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered:
    print(f"Conquered peaks:")
    for p in conquered:
        print(p)